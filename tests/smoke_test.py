from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "qt-ui-inspector"


def validate_skill() -> None:
    from dcc_mcp_core import validate_skill

    report = validate_skill(str(SKILL))
    assert not report.has_errors, report


def wrappers_import() -> None:
    for script in (SKILL / "scripts").glob("*.py"):
        text = script.read_text(encoding="utf-8")
        assert "dcc_mcp_core.skills.qt_ui_inspector" in text, script


def main() -> None:
    validate_skill()
    wrappers_import()


if __name__ == "__main__":
    main()
