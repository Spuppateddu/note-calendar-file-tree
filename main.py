#!/usr/bin/env python3

import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Tuple
import argparse
from dotenv import load_dotenv

def parse_date(date_str: Optional[str]) -> datetime:
    """Parse date string in YYYY-MM-DD format"""
    if date_str:
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print(f"Error: Invalid date format. Please use YYYY-MM-DD format. Got: {date_str}")
            sys.exit(1)
    return datetime.now()

def get_date_range() -> Tuple[datetime, datetime]:
    """Get start and end dates from command line arguments or use defaults"""
    parser = argparse.ArgumentParser(description='Generate calendar folder structure')
    parser.add_argument('start_date', nargs='?', help='Start date (YYYY-MM-DD)', default=None)
    parser.add_argument('end_date', nargs='?', help='End date (YYYY-MM-DD)', default=None)

    args = parser.parse_args()

    start_date = parse_date(args.start_date)
    if args.end_date:
        end_date = parse_date(args.end_date)
    else:
        # If no end date provided, use start date + 5 years
        end_date = start_date + timedelta(days=365 * 5)

    return start_date, end_date

def create_calendar_structure(base_path: str, start_date: datetime, end_date: datetime):
    """Create the calendar folder structure"""
    current_date = start_date
    base_path = Path(base_path)

    # Create the base directory first
    base_path.mkdir(exist_ok=True)

    while current_date <= end_date:
        # Create folder structure: YYYY/MM-Month/DD-DayOfWeek
        year_folder = base_path / str(current_date.year)
        # Format month as "MM-MonthName" (e.g., "01-January")
        month_folder = year_folder / f"{current_date.strftime('%m-%B')}"
        # Format day as "DD-DayOfWeek" (e.g., "01-Monday")
        day_folder = month_folder / f"{current_date.strftime('%d-%A')}"

        # Create folders if they don't exist
        year_folder.mkdir(exist_ok=True)
        month_folder.mkdir(exist_ok=True)
        day_folder.mkdir(exist_ok=True)

        current_date += timedelta(days=1)

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Get base path from environment variable or use default
    base_path = os.getenv('CALENDAR_BASE_PATH', './calendar')

    # Get date range
    start_date, end_date = get_date_range()

    print(f"Generating calendar structure from {start_date.date()} to {end_date.date()}")
    print(f"Base path: {base_path}")

    # Create the folder structure
    create_calendar_structure(base_path, start_date, end_date)
    print("Calendar structure generated successfully!")

if __name__ == "__main__":
    main()
