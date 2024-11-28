import csv
from datetime import datetime

def update_summary(scan_type, target, vulnerabilities, details_file):
    summary_file = "outputs/summary.csv"
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create the summary file with headers if it doesn't exist
    try:
        with open(summary_file, 'r') as f:
            pass
    except FileNotFoundError:
        with open(summary_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Scan Type", "Target", "Vulnerabilities Found", "Date", "Details File"])

    # Append a new entry to the summary CSV
    with open(summary_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([scan_type, target, vulnerabilities, date, details_file])
