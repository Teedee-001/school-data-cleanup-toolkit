
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from duplicate_checker import find_duplicates


def test_detect_duplicate_student_id():
    records = [
        {"student_id": "ST001"},
        {"student_id": "ST002"},
        {"student_id": "ST001"}
    ]

    duplicates = find_duplicates(records)

    assert len(duplicates) == 1
    assert "ST001" in duplicates[0]


def test_no_duplicates():
    records = [
        {"student_id": "ST001"},
        {"student_id": "ST002"}
    ]

    duplicates = find_duplicates(records)

    assert duplicates == []
