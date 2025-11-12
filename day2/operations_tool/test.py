from pathlib import Path

from .main import process_file

in_file = "day2/operations_tool/sample_files/operations.txt"
out_file = "day2/operations_tool/sample_files/results_test.txt"

process_file(in_file, out_file)
print(Path(out_file).read_text())
