# DCC-MCP Qt UI Inspector

Reusable Qt UI inspection for DCC-MCP.

This package exposes the core `qt-ui-inspector` skill as an installable
marketplace repo. It is read-only: list Qt windows, find widgets, describe
widgets, snapshot widget trees, and wait for widgets in PySide/PyQt hosts.

## Install

```bash
dcc-mcp-cli marketplace add dcc-mcp/dcc-ui-qt-inspector
dcc-mcp-cli marketplace install dcc-ui-qt-inspector
```

## Tools

- `list_windows`
- `find_widgets`
- `describe_widget`
- `snapshot_tree`
- `wait_for_widget`

Use `dcc-ui-qt-actions` for clicks, text entry, screenshots, and other UI
mutations.
