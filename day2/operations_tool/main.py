# day2/operations_tool/main.py
import sys
from typing import List

from .evaluator import evaluate
from .io_utils import read_operations, write_results
from .parser import parse_and_validate


def process_file(input_path: str, output_path: str) -> None:
    operations = read_operations(input_path)
    results: List[str] = []
    for line in operations:
        try:
            tree = parse_and_validate(line)
            value = evaluate(tree)
            results.append(f"{line} = {value}")
        except Exception as e:
            results.append(f"{line} -> ERROR: {e}")
    write_results(output_path, results)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python -m day2.operations_tool.main <input_path> <output_path>")
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    process_file(input_path, output_path)
    print("Traitement terminé.")
