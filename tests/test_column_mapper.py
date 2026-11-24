
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from column_mapper import map_columns


def test_map_alternative_headers():
    headers = [
        "Matric Number",
        "Full Name",
        "Email Address",
        "Age",
        "Class Level"
    ]

    mapping = map_columns(headers)

    assert mapping["Matric Number"] == "student_id"
    assert mapping["Full Name"] == "student_name"
    assert mapping["Email Address"] == "email"
    assert mapping["Age"] == "age"
    assert mapping["Class Level"] == "class"
