#!/usr/bin/env python3

import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

LEETCODE_DIR = BASE_DIR / "leetcode"
TESTCASE_DIR = BASE_DIR / "leetcode_testcases"

LEETCODE_DIR.mkdir(parents=True, exist_ok=True)
TESTCASE_DIR.mkdir(parents=True, exist_ok=True)


def create_solution_file(path: Path):
    path.write_text(
'''# Copy from Leetcode terminal
''',
        encoding="utf-8"
    )

    os.chmod(path, 0o777)

def main():
    print("=" * 60)
    print("LeetCode File Generator")
    print("=" * 60)

    number = input("LeetCode Problem Number : ").strip()
    name = input("Problem Name            : ").strip()

    solution_path = LEETCODE_DIR / f"LeetCode {number} - {name}.py"

    if solution_path.exists():
        print(f"\n❌ {solution_path.name} already exists.")
    else:
        create_solution_file(solution_path)
        print(f"✅ Created {solution_path.name}")

    print("\nDone.")


if __name__ == "__main__":
    main()