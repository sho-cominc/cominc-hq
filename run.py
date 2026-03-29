"""ComInc. Agent System — standalone entry point.

Works regardless of working directory:
    python run.py
    python run.py "タスク"
    python run.py --agent cat "SEO audit"
"""
import os
import sys

# Fix Windows encoding BEFORE any print/import that might output unicode
os.environ["PYTHONIOENCODING"] = "utf-8"
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

from pathlib import Path

# Ensure project root is on sys.path so `src.*` imports work
project_root = Path(__file__).parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.main import main

main()
