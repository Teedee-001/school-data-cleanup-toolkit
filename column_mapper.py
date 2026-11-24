
def map_columns(headers):
    """Map common school spreadsheet headers to standard names."""

    aliases = {
        "student_id": [
            "student_id", "student id", "matric number",
            "registration number", "admission number"
        ],
        "student_name": [
            "student_name", "student name", "full name",
            "name", "learner name"
        ],
        "email": [
            "email", "email address", "student email"
        ],
        "age": [
            "age", "student age"
        ],
        "class": [
            "class", "class level", "grade", "level"
        ]
    }

    mapping = {}

    for header in headers:
        normalized_header = header.strip().lower()

        for standard_name, possible_names in aliases.items():
            if normalized_header in possible_names:
                mapping[header] = standard_name
                break

    return mapping
