
def validate_records(records):
    """Check student records for missing or invalid values."""

    issues = []

    required_fields = [
        "student_id",
        "student_name",
        "email",
        "age",
        "class"
    ]

    for row_number, record in enumerate(records, start=2):

        for field in required_fields:
            if not record.get(field) or not record[field].strip():
                issues.append(
                    f"Row {row_number}: {field} is missing."
                )

        email = record.get("email", "").strip()

        if email and ("@" not in email or "." not in email.split("@")[-1]):
            issues.append(
                f"Row {row_number}: Invalid email address."
            )

        age = record.get("age", "").strip()

        if age:
            try:
                age_number = int(age)

                if age_number < 3 or age_number > 100:
                    issues.append(
                        f"Row {row_number}: Age is outside the valid range."
                    )

            except ValueError:
                issues.append(
                    f"Row {row_number}: Age must be a number."
                )

    return issues
