#!/usr/bin/env python3
"""Frontmatter description must be a single-line quoted scalar (not folded)."""
from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
SJ = ROOT / "skill.json"

REQUIRED = (
    "必须使用本技能",
    "不确定时默认使用",
    "禁止跳过",
    "查一下这个公司",
    "看下这个JD",
    "/job-research-analyst",
)


class TestSkillFrontmatter(unittest.TestCase):
    def test_description_single_line_quoted_matches_skill_json(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---"), "SKILL.md must start with YAML frontmatter")
        parts = text.split("---", 2)
        self.assertGreaterEqual(len(parts), 3, "SKILL.md frontmatter must be closed")
        fm = parts[1]
        self.assertIsNone(
            re.search(r"^description:\s*[>|]", fm, re.M),
            "description must not use folded/literal block scalar",
        )
        m = re.search(r'^description:\s+"(.*)"\s*$', fm, re.M)
        self.assertIsNotNone(m, "description must be a single-line double-quoted scalar")
        desc = m.group(1)
        self.assertGreaterEqual(len(desc), 1)
        self.assertLessEqual(len(desc), 1024)
        sj = json.loads(SJ.read_text(encoding="utf-8"))
        self.assertEqual(sj["description"], desc)
        for token in REQUIRED:
            with self.subTest(token=token):
                self.assertIn(token, desc)


if __name__ == "__main__":
    unittest.main()
