
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from importer import import_csv


def test_import_valid_csv(tmp_path):
    csv_file = tmp_path / "students.csv"

    csv_file.write_text(
        "student_id,student_name,email,age,class\n"
        "ST001,John Doe,john@gmail.com,15,SS1\n",
        encoding="utf-8"
    )

    records, errors = import_csv(csv_file)

    assert len(records) == 1
    assert records[0]["student_id"] == "ST001"
    assert errors == []


def test_missing_csv_file():
    records, errors = import_csv("missing_file.csv")

    assert records == []
    assert "File not found." in errors
