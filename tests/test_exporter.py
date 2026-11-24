
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from exporter import export_csv


def test_export_records(tmp_path):
    records = [
        {
            "student_id": "ST001",
            "student_name": "John Doe",
            "email": "john@gmail.com",
            "age": "15",
            "class": "SS1"
        }
    ]

    output_file = tmp_path / "reports" / "cleaned.csv"

    success, message = export_csv(records, output_file)

    assert success is True
    assert output_file.exists()
    assert "Cleaned data exported" in message


def test_export_empty_records(tmp_path):
    output_file = tmp_path / "cleaned.csv"

    success, message = export_csv([], output_file)

    assert success is False
    assert "No records available" in message
