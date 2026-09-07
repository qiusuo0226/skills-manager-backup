# scripts/

## validate_deliverables.py

校验三件套结构。失败禁止交付。标准库即可，不依赖 python-docx / openpyxl。

```
python scripts/validate_deliverables.py --dir <交付目录>
python scripts/validate_deliverables.py --files <f1> <f2> ...
python scripts/validate_deliverables.py --dir <交付目录> --allow-partial
```

`--dir` 且无 `--allow-partial`：三类文件各至少 1 个。`--files` 只校验列出的文件。

冻结标题与表头必须与 `references/report-templates.md` 逐字相同。
