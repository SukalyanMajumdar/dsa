import json
import importlib.util
from pathlib import Path


BASE_DIR = Path(__file__).parent
LEETCODE_DIR = BASE_DIR / "leetcode"
TESTCASE_DIR = BASE_DIR / "leetcode_testcases"


def find_file(directory: Path, problem_number: str):
    matches = list(directory.glob(f"LeetCode {problem_number} -*"))

    if not matches:
        raise FileNotFoundError(
            f"Could not find problem {problem_number} inside {directory}"
        )

    return matches[0]


def load_solution(filepath: Path):
    spec = importlib.util.spec_from_file_location("solution_module", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module.Solution()


def get_solution_method(solution):
    methods = [
        getattr(solution, name)
        for name in dir(solution)
        if callable(getattr(solution, name))
        and not name.startswith("__")
    ]

    if len(methods) != 1:
        raise Exception(
            f"Expected exactly one public method inside Solution. Found {len(methods)}."
        )

    return methods[0]


def load_tests(filepath: Path):
    with open(filepath, "r") as f:
        return json.load(f)


def run_tests(method, tests):
    passed = 0

    print("=" * 70)

    for i, test in enumerate(tests, start=1):

        inputs = test[0]
        expected = test[1]

        actual = method(*inputs)

        print(f"Test {i}")
        print(f"Input    : {inputs}")
        print(f"Expected : {expected}")
        print(f"Actual   : {actual}")

        if actual == expected:
            print("Result   : ✅ PASS")
            passed += 1
        else:
            print("Result   : ❌ FAIL")

        print("-" * 70)

    print(f"\nPassed {passed}/{len(tests)}")

def main():

    problem = input("Enter LeetCode Problem Number: ").strip()

    solution_file = find_file(LEETCODE_DIR, problem)
    testcase_file = find_file(TESTCASE_DIR, problem)

    print(f"\nSolution : {solution_file.name}")
    print(f"Testcase : {testcase_file.name}\n")

    solution = load_solution(solution_file)

    method = get_solution_method(solution)

    tests = load_tests(testcase_file)

    run_tests(method, tests)


if __name__ == "__main__":
    main()