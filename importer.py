
import csv
from column_mapper import map_columns


def import_csv(file_path):
    """Import student records using flexible column mapping."""

    records = []
    errors = []

    required_columns = [
        "student_id",
        "student_name",
        "email",
        "age",
        "class"
    ]

    try:
        with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames:
                return [], ["The CSV file is empty or has no headers."]

            mapping = map_columns(reader.fieldnames)

            mapped_columns = list(mapping.values())

            if len(mapped_columns) != len(set(mapped_columns)):
                return [], ["Multiple headers map to the same standard field."]

            missing_columns = [
                column for column in required_columns
                if column not in mapped_columns
            ]

            if missing_columns:
                return [], [
                    f"Could not identify these required columns: {', '.join(missing_columns)}"
                ]

            for row_number, row in enumerate(reader, start=2):

                if None in row:
                    errors.append(f"Row {row_number}: Extra values found.")
                    continue

                if any(value is None for value in row.values()):
                    errors.append(f"Row {row_number}: Some fields are missing.")
                    continue

                mapped_record = {
                    standard_name: row[original_name]
                    for original_name, standard_name in mapping.items()
                }

                records.append(mapped_record)

    except FileNotFoundError:
        errors.append("File not found.")
    except UnicodeDecodeError:
        errors.append("The file has an unsupported text encoding.")
    except csv.Error as error:
        errors.append(f"CSV reading error: {error}")
    except OSError as error:
        errors.append(f"File access error: {error}")

    return records, errors
