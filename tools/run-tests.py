#!/usr/bin/env python3
"""Run every historical executable test plus syntax and data checks."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"


def commands() -> list[list[str]]:
    result: list[list[str]] = []
    for path in sorted(TOOLS.glob("audit-*.py")) + sorted(TOOLS.glob("test-*.py")):
        result.append([sys.executable, str(path.relative_to(ROOT))])
    for path in sorted(TOOLS.glob("test-*.cjs")):
        result.append(["node", str(path.relative_to(ROOT))])
    for path in sorted((ROOT / "assets" / "scripts").glob("*.js")):
        result.append(["node", "--check", str(path.relative_to(ROOT))])
    result.append(["node", "--check", "service-worker.js"])
    return result


def validate_json() -> int:
    count = 0
    for path in sorted((ROOT / "data").glob("*.json")):
        json.loads(path.read_text(encoding="utf-8"))
        count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rounds", type=int, default=1)
    args = parser.parse_args()
    if args.rounds < 1:
        raise SystemExit("--rounds deve ser maior que zero")
    suite = commands()
    total = 0
    for round_number in range(1, args.rounds + 1):
        print(f"\n=== Rodada {round_number}/{args.rounds} ===")
        for command in suite:
            completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
            total += 1
            label = " ".join(command)
            if completed.returncode:
                print(f"FALHOU: {label}\n{completed.stdout}{completed.stderr}")
                raise SystemExit(completed.returncode)
        json_count = validate_json()
        print(f"OK: {len(suite)} executáveis + {json_count} JSON")
    print(f"\nSUCESSO: {total} execuções em {args.rounds} rodada(s).")


if __name__ == "__main__":
    main()
