# SQL Inventory Project
A command-line inventory analysis tool built with Python and SQLite.

## What It Does

Generates reports from a structured inventory database, organized by searchable categories including department, price, product, and quantity. Reports include:

- Full inventory list
- Low stock alerts (under 25 units)
- Average price by category
- Total inventory dollar value

Access to these insights supports forecasting, profit margin analysis, and identifying key volume drivers within categories.

## Skills Demonstrated

- SQLite database creation and management
- SQL queries: SELECT, WHERE, GROUP BY, SUM, AVG
- Duplicate-safe data insertion pattern
- Python and SQL integration via sqlite3

## How to Run

1. Clone the repo
2. Run `python ex12_sql_project.py`
3. A local `inventory.db` file will be created automatically

## Tech Stack

- Python 3
- SQLite3 (built-in)
