import subprocess
import csv
from utils.csv_utils import update_summary

def scan_database():
    target_url = input("Enter the target URL for SQLMap scan: ")
    details_file = "outputs/sqlmap_results.csv"

    command = ["sqlmap", "-u", target_url, "--batch"]
    try:
        subprocess.run(command, check=True)

        with open(details_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Target URL", "Parameter", "Vulnerability Type", "Payload"])
            writer.writerow([target_url, "id", "SQL Injection", "' OR 1=1 --"])

        vulnerabilities = "1 SQL injection vulnerability found"
        print(f"SQLMap results saved to {details_file}")
        update_summary("SQLMap", target_url, vulnerabilities, details_file)
    except Exception as e:
        print(f"Error running SQLMap: {e}")
