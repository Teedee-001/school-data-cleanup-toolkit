import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from validator import validate_records


def test_missing_email():
    records = [
        {
            "student_id": "ST001",
            "student_name": "John Doe",
            "email": "",
            "age": "15",
            "class": "SS1"
        }
    ]

    issues = validate_records(records)

    assert any("email is missing" in issue for issue in issues)


def test_invalid_age():
    records = [
        {
            "student_id": "ST002",
            "student_name": "Jane Smith",
            "email": "jane@gmail.com",
            "age": "abc",
            "class": "SS2"
        }
    ]

    issues = validate_records(records)

    assert any("Age must be a number" in issue for issue in issues)


def test_valid_record():
    records = [
        {
            "student_id": "ST003",
            "student_name": "Peter James",
            "email": "peter@gmail.com",
            "age": "14",
            "class": "SS1"
        }
    ]

    issues = validate_records(records)

    assert issues == []
