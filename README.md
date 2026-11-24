# School Data Cleanup & Validation Toolkit

## Project Overview

The School Data Cleanup & Validation Toolkit is a Python-based command-line application designed to help schools identify, review, and correct errors in student records stored in CSV files.

It supports different school spreadsheet formats through flexible column mapping.

## Features

- CSV file importing
- Automatic detection of missing fields
- Email and age validation
- Duplicate student ID detection
- Manual correction of student records
- Export of reviewed records to CSV
- Flexible column mapping for different school headers
- Automated tests using pytest

## Technologies Used

- Python
- CSV module
- Pytest
- Git and GitHub

## Project Structure

```text
school-data-cleanup-toolkit/
│
├── data/
├── reports/
├── tests/
├── Screenshots/
├── main.py
├── importer.py
├── validator.py
├── duplicate_checker.py
├── column_mapper.py
├── exporter.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone or download this repository.
2. Open the project folder in your terminal.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

```bash
python main.py
```

Press Enter to use the sample dataset, or provide the path to another CSV file.

## Testing

Run the automated tests:

```bash
pytest -v
```

The tests cover CSV importing, field validation, duplicate detection, exporting, and column mapping.

## Sample Data

The `data` folder contains synthetic student records for testing. No real student information is used.

## AI Use Reflection

AI tools were used as learning and development assistants to help understand Python concepts, debug errors, and improve code structure. The implementation and test results were reviewed and verified during development.

## Limitations

- The application currently supports CSV files.
- Column mapping uses predefined aliases rather than an AI model.
- Record
