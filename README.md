# Calendar Folder Structure Generator

This script generates a hierarchical folder structure for calendar dates in the format:
```
YYYY/
  MM-Month/
    DD-DayOfWeek/
```

## Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The script can be run in several ways:

1. Generate calendar structure for the next 5 years starting from today:
```bash
python3 main.py
```

2. Generate calendar structure from a specific start date to 5 years ahead:
```bash
python3 main.py 2025-01-01
```

3. Generate calendar structure for a specific date range:
```bash
python3 main.py 2025-01-01 2027-01-01
```

## Output Structure

The script will create a folder structure like this:
```
calendar/
  2025/
    01-January/
      01-Wednesday/
      02-Thursday/
      ...
    02-February/
      ...
  2026/
    ...
```

All folders are created only if they don't already exist, so it's safe to run the script multiple times.
