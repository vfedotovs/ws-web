#!/usr/bin/env python3
"""
PostgreSQL Dump to CSV Converter

This script extracts tables from a PostgreSQL dump file (.sql) and converts them to CSV files.
It parses COPY ... FROM stdin blocks directly without requiring a database connection.

Usage:
    python pg_dump_to_csv.py <sql_file> [output_dir]

Examples:
    python pg_dump_to_csv.py pg_backup_2025_11_03.sql
    python pg_dump_to_csv.py pg_backup_2025_11_03.sql csv_output
"""

import re
import csv
import sys
from pathlib import Path


def extract_tables_from_pg_dump(sql_file_path, output_dir='.'):
    """
    Extract tables from PostgreSQL dump and convert to CSV files.

    Args:
        sql_file_path: Path to the .sql dump file
        output_dir: Directory to save CSV files (default: current directory)

    Returns:
        List of tuples (table_name, row_count) for extracted tables
    """
    sql_file_path = Path(sql_file_path)
    output_dir = Path(output_dir)

    # Validate input file exists
    if not sql_file_path.exists():
        print(f"Error: SQL file not found: {sql_file_path}")
        sys.exit(1)

    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True, parents=True)

    print(f"Reading SQL dump from: {sql_file_path}")
    print(f"Output directory: {output_dir.absolute()}\n")

    # Read the SQL dump file
    try:
        with open(sql_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    # Find all COPY statements with their data
    # Pattern matches: COPY table_name (columns) FROM stdin; ... \.
    copy_pattern = r'COPY\s+(\S+)\s*\((.*?)\)\s+FROM\s+stdin;(.*?)\n\\.\n'
    matches = re.finditer(copy_pattern, content, re.DOTALL)

    tables_extracted = []

    for match in matches:
        # Extract table name (remove schema prefix if present)
        table_name = match.group(1).replace('public.', '')

        # Extract column names
        columns = [col.strip() for col in match.group(2).split(',')]

        # Extract data block
        data_block = match.group(3).strip()

        # Parse data rows (PostgreSQL COPY format uses tabs as delimiters)
        rows = []
        for line in data_block.split('\n'):
            if line.strip():
                # Split by tab character
                row = line.split('\t')
                # Replace \N with empty string (PostgreSQL NULL representation)
                row = ['' if val == '\\N' else val for val in row]
                rows.append(row)

        # Write to CSV file
        csv_filename = output_dir / f'{table_name}.csv'
        try:
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(columns)  # Write header
                writer.writerows(rows)     # Write data rows

            tables_extracted.append((table_name, len(rows)))
            print(f"✓ Extracted '{table_name}': {len(rows)} rows → {csv_filename.name}")

        except Exception as e:
            print(f"✗ Error writing {table_name}.csv: {e}")

    return tables_extracted


def main():
    """Main entry point for the script."""
    # Parse command line arguments
    if len(sys.argv) < 2:
        print(__doc__)
        print("Error: SQL file path is required")
        sys.exit(1)

    sql_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else 'csv_output'

    # Extract tables
    tables = extract_tables_from_pg_dump(sql_file, output_dir)

    # Print summary
    print(f"\n{'='*60}")
    print(f"Summary: Extracted {len(tables)} table(s)")
    print(f"{'='*60}")

    if tables:
        total_rows = sum(count for _, count in tables)
        for table_name, row_count in tables:
            print(f"  • {table_name}: {row_count:,} rows")
        print(f"\nTotal rows exported: {total_rows:,}")
    else:
        print("No tables found in the dump file.")
        print("\nNote: This script only processes COPY ... FROM stdin blocks.")
        print("If your dump uses INSERT statements, you'll need a different approach.")


if __name__ == '__main__':
    main()
