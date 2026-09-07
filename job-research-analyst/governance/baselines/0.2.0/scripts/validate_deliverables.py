#!/usr/bin/env python3
"""Validate job-research-analyst deliverable structure.

Frozen strings must match references/report-templates.md verbatim.
"""
from __future__ import annotations

import argparse
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

NS_W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
NS_MAIN = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
NS_REL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
NS_PKGREL = "{http://schemas.openxmlformats.org/package/2006/relationships}"

DOCX_NAME = re.compile(r"^.+_深度介绍_\d{8}\.docx$")
XLSX_SALARY_NAME = re.compile(r"^.+_薪资福利对比_\d{8}\.xlsx$")
XLSX_REVIEW_NAME = re.compile(r"^.+_员工评价与风险提示_\d{8}\.xlsx$")

DOCX_REQUIRED_HEADINGS = [
    "报告摘要与核心结论",
    "岗位 JD 解读",
    "公司基本信息",
    "股权与关联方",
    "业务与行业地位",
    "扩张与收缩信号",
    "财务健康度",
    "组织与职级体系",
    "个人匹配度分析与面试建议",
    "信息来源清单",
    "岗位基本信息",
    "岗位职责与要求解读",
    "异常点提示",
    "用户背景摘要",
    "与岗位要求逐条对照",
    "匹配点与差距点",
    "投递与面试策略",
]

SALARY_SHEETS = {
    "薪资对比": [
        "公司名",
        "岗位名称",
        "城市",
        "挂牌薪资区间(税前/月)",
        "年薪月数",
        "经验要求",
        "样本量",
        "薪资中位数",
        "年终奖",
        "绩效占比",
        "补贴",
        "数据来源",
        "采集时间",
    ],
    "福利待遇对比": [
        "公司名",
        "社保公积金基数",
        "公积金比例",
        "补充医疗",
        "带薪年假",
        "加班调休/加班费",
        "餐补/交通补",
        "出差补贴",
        "其他福利",
        "信息来源",
    ],
    "用户目标薪资匹配度": ["项目", "用户当前", "用户目标", "公司A", "公司B", "公司C"],
}

REVIEW_SHEETS = {
    "员工评价汇总": [
        "维度",
        "评分/评价",
        "评价条数",
        "正面评价摘要",
        "负面评价摘要",
        "评价主体",
        "数据来源",
        "时间范围",
    ],
    "风险提示清单": [
        "风险等级",
        "风险类型",
        "具体描述",
        "证据来源",
        "证据等级",
        "对用户的影响",
        "建议",
    ],
    "面试建议提问清单": ["关注方向", "建议提问", "目的"],
}

FROZEN_STRINGS = (
    DOCX_REQUIRED_HEADINGS
    + list(SALARY_SHEETS.keys())
    + [h for cols in SALARY_SHEETS.values() for h in cols]
    + list(REVIEW_SHEETS.keys())
    + [h for cols in REVIEW_SHEETS.values() for h in cols]
)


def docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as zf:
        xml = zf.read("word/document.xml")
    root = ET.fromstring(xml)
    parts: list[str] = []
    for t in root.iter(f"{NS_W}t"):
        if t.text:
            parts.append(t.text)
        if t.tail:
            parts.append(t.tail)
    return "".join(parts)


def col_index(cell_ref: str) -> int:
    letters = "".join(c for c in cell_ref if c.isalpha())
    n = 0
    for c in letters:
        n = n * 26 + (ord(c.upper()) - 64)
    return n - 1


def load_shared_strings(zf: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []
    root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    out: list[str] = []
    for si in root.findall(f"{NS_MAIN}si"):
        texts = [t.text or "" for t in si.iter(f"{NS_MAIN}t")]
        out.append("".join(texts))
    return out


def cell_value(c: ET.Element, shared: list[str]) -> str:
    t = c.get("t")
    is_el = c.find(f"{NS_MAIN}is")
    if t == "inlineStr" and is_el is not None:
        return "".join((n.text or "") for n in is_el.iter(f"{NS_MAIN}t"))
    v = c.find(f"{NS_MAIN}v")
    if v is None or v.text is None:
        return ""
    if t == "s":
        return shared[int(v.text)]
    return v.text


def sheet_paths(zf: zipfile.ZipFile) -> dict[str, str]:
    wb = ET.fromstring(zf.read("xl/workbook.xml"))
    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    rid_to_target = {}
    for rel in rels:
        rid = rel.get("Id")
        target = rel.get("Target")
        if rid and target:
            rid_to_target[rid] = target.lstrip("/")
    out: dict[str, str] = {}
    for sh in wb.findall(f"{NS_MAIN}sheets/{NS_MAIN}sheet"):
        name = sh.get("name") or ""
        rid = sh.get(f"{NS_REL}id")
        target = rid_to_target.get(rid or "", "")
        if target and not target.startswith("xl/"):
            target = "xl/" + target
        out[name] = target
    return out


def first_row(zf: zipfile.ZipFile, sheet_path: str, shared: list[str]) -> list[str]:
    root = ET.fromstring(zf.read(sheet_path))
    sheet_data = root.find(f"{NS_MAIN}sheetData")
    if sheet_data is None:
        return []
    row = sheet_data.find(f"{NS_MAIN}row")
    if row is None:
        return []
    cells: dict[int, str] = {}
    max_i = -1
    for c in row.findall(f"{NS_MAIN}c"):
        ref = c.get("r") or "A1"
        i = col_index(ref)
        cells[i] = cell_value(c, shared)
        max_i = max(max_i, i)
    return [cells.get(i, "") for i in range(max_i + 1)]


def check_docx(path: Path, missing: list[str]) -> None:
    if not DOCX_NAME.match(path.name):
        missing.append(f"{path.name}: 文件名不符合 {{公司名}}_深度介绍_YYYYMMDD.docx")
    try:
        text = docx_text(path)
    except Exception as e:
        missing.append(f"{path.name}: 无法读取 docx ({e})")
        return
    for h in DOCX_REQUIRED_HEADINGS:
        if h not in text:
            missing.append(f"{path.name}: 缺少标题「{h}」")


def check_xlsx(path: Path, expected: dict[str, list[str]], name_re: re.Pattern[str], kind: str, missing: list[str]) -> None:
    if not name_re.match(path.name):
        missing.append(f"{path.name}: 文件名不符合 {kind}")
    try:
        with zipfile.ZipFile(path) as zf:
            shared = load_shared_strings(zf)
            sheets = sheet_paths(zf)
            for sheet_name, headers in expected.items():
                if sheet_name not in sheets:
                    missing.append(f"{path.name}: 缺少 Sheet「{sheet_name}」")
                    continue
                row = first_row(zf, sheets[sheet_name], shared)
                if len(row) < len(headers) or row[: len(headers)] != headers:
                    missing.append(
                        f"{path.name}: Sheet「{sheet_name}」表头应为 {headers}（左侧顺序冻结，右侧可追加）"
                    )
    except Exception as e:
        missing.append(f"{path.name}: 无法读取 xlsx ({e})")


def classify(path: Path) -> str | None:
    n = path.name
    if DOCX_NAME.match(n):
        return "docx"
    if XLSX_SALARY_NAME.match(n):
        return "salary"
    if XLSX_REVIEW_NAME.match(n):
        return "review"
    return None


def main() -> int:
    p = argparse.ArgumentParser(description="Validate job-research-analyst deliverables")
    p.add_argument("--dir", type=Path, help="Directory containing the three-pack")
    p.add_argument("--files", nargs="+", type=Path, help="Explicit files")
    p.add_argument("--allow-partial", action="store_true", help="Do not require all three types")
    args = p.parse_args()

    files: list[Path] = []
    if args.files:
        files.extend(args.files)
    if args.dir:
        d = args.dir
        if not d.is_dir():
            print(f"ERROR: not a directory: {d}", file=sys.stderr)
            return 2
        files.extend(sorted(x for x in d.iterdir() if x.is_file()))
    if not files:
        print("ERROR: pass --dir or --files", file=sys.stderr)
        return 2

    missing: list[str] = []
    kinds: set[str] = set()
    unmatched = []
    for f in files:
        kind = classify(f)
        if kind is None:
            if args.files and f in (args.files or []):
                unmatched.append(f.name)
            continue
        kinds.add(kind)
        if kind == "docx":
            check_docx(f, missing)
        elif kind == "salary":
            check_xlsx(f, SALARY_SHEETS, XLSX_SALARY_NAME, "{岗位方向}_薪资福利对比_YYYYMMDD.xlsx", missing)
        else:
            check_xlsx(f, REVIEW_SHEETS, XLSX_REVIEW_NAME, "{公司名}_员工评价与风险提示_YYYYMMDD.xlsx", missing)

    if args.files:
        for name in unmatched:
            missing.append(f"{name}: 文件名不符合三件套命名")

    require_all = bool(args.dir) and not args.allow_partial and not args.files
    if require_all:
        if "docx" not in kinds:
            missing.append("目录中缺少 *_深度介绍_YYYYMMDD.docx")
        if "salary" not in kinds:
            missing.append("目录中缺少 *_薪资福利对比_YYYYMMDD.xlsx")
        if "review" not in kinds:
            missing.append("目录中缺少 *_员工评价与风险提示_YYYYMMDD.xlsx")

    if missing:
        print("校验失败：")
        for m in missing:
            print(f"  - {m}")
        return 1
    print("ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
