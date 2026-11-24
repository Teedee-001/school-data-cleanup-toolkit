
from pathlib import Path

from importer import import_csv
from validator import validate_records
from duplicate_checker import find_duplicates
from exporter import export_csv


def main():
    print("\n====================================")
    print(" SCHOOL DATA CLEANUP TOOLKIT")
    print("====================================")

    file_path = input(
        "\nEnter CSV file path (press Enter for sample data): "
    ).strip()

    if not file_path:
        file_path = Path(__file__).parent / "data" / "sample_students.csv"

    records, import_errors = import_csv(file_path)

    if import_errors:
        print("\nIMPORT ERRORS:")
        for error in import_errors:
            print("-", error)

    if not records:
        print("\nNo records available. Exiting.")
        return

    print(f"\nSuccessfully imported {len(records)} records.")

    while True:
        print("\nSTUDENT RECORDS:")
        for row_number, record in enumerate(records, start=2):
            print(f"\nRow {row_number}: {record}")

        print("\nFIELD VALIDATION RESULTS:")
        validation_issues = validate_records(records)

        if validation_issues:
            for issue in validation_issues:
                print("-", issue)
        else:
            print("No validation issues found.")

        print("\nDUPLICATE DETECTION RESULTS:")
        duplicate_issues = find_duplicates(records)

        if duplicate_issues:
            for issue in duplicate_issues:
                print("-", issue)
        else:
            print("No duplicate records found.")

        choice = input("\nDo you want to edit a record? (y/n): ").strip().lower()

        if choice != "y":
            break

        try:
            row_number = int(input("Enter row number to edit: "))

            if row_number < 2 or row_number > len(records) + 1:
                print("Invalid row number.")
                continue

            field = input(
                "Enter field name (student_id, student_name, email, age, class): "
            ).strip()

            if field not in records[row_number - 2]:
                print("Invalid field name.")
                continue

            new_value = input("Enter corrected value: ").strip()
            records[row_number - 2][field] = new_value

            print("Record updated successfully.")

        except ValueError:
            print("Please enter a valid row number.")

    validation_issues = validate_records(records)
    duplicate_issues = find_duplicates(records)

    print("\nFINAL REVIEW:")
    print("Remaining validation issues:", len(validation_issues))
    print("Remaining duplicate issues:", len(duplicate_issues))

    if validation_issues or duplicate_issues:
        print("\nRecords still contain issues.")
        choice = input("Export anyway? (y/n): ").strip().lower()

        if choice != "y":
            print("Export cancelled.")
            return

    output_path = Path(__file__).parent / "reports" / "cleaned_students.csv"

    success, message = export_csv(records, output_path)
    print(message)

    print("\nThank you for using the toolkit!")


if __name__ == "__main__":
    main()
