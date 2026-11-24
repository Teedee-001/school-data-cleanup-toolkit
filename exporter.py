
import csv
from pathlib import Path


def export_csv(records, file_path):
    """Export reviewed student records to a CSV file."""

    if not records:
        return False, "No records available to export."

    output_path = Path(file_path)

    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)

        fieldnames = list(records[0].keys())

        with open(output_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(records)

        return True, f"Cleaned data exported to {output_path}"

    except (OSError, csv.Error) as error:
        return False, f"Export failed: {error}"
