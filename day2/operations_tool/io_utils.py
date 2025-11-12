# day2/operations_tool/io_utils.py
from pathlib import Path
from typing import List


def read_operations(file_path: str) -> List[str]:
    p = Path(file_path)
    if not p.exists():
        raise FileNotFoundError(f"{file_path} n'existe pas.")
    lines = p.read_text(encoding="utf8").splitlines()
    # filter comments and blank lines
    cleaned = []
    for l in lines:
        l = l.strip()
        if not l or l.startswith("#"):
            continue
        cleaned.append(l)
    return cleaned


def write_results(file_path: str, results: List[str]) -> None:
    p = Path(file_path)
    p.write_text("\n".join(results) + "\n", encoding="utf8")
