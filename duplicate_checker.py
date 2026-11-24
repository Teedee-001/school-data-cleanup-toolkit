
def find_duplicates(records):
    """Identify records with repeated student IDs."""

    seen_ids = set()
    duplicates = []

    for row_number, record in enumerate(records, start=2):
        student_id = record.get("student_id", "").strip()

        if not student_id:
            continue

        if student_id in seen_ids:
            duplicates.append(
                f"Row {row_number}: Duplicate student ID '{student_id}'."
            )
        else:
            seen_ids.add(student_id)

    return duplicates
