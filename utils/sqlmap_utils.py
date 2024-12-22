import subprocess
import csv
from utils.csv_utils import update_summary

# Output file for detailed SQLMap results
SQLMAP_RESULTS_FILE = "outputs/sqlmap_results.csv"

def scan_database():
    """Perform a database vulnerability scan using SQLMap."""
    target_url = input("Enter the target URL for SQLMap scan (e.g., http://example.com): ")
    
    # Command to run SQLMap
    command = ["sqlmap", "-u", target_url, "--batch"]
    
    try:
        print("Starting SQLMap scan...")
        subprocess.run(command, check=True)  # Run the SQLMap command
        
        # Simulate results for demonstration purposes (replace with actual parsing of SQLMap results)
        vulnerabilities = [
            {
                "Target URL": target_url,
                "Parameter": "id",
                "Vulnerability Type": "SQL Injection",
                "Payload": "' OR 1=1 --"
            }
        ]
        
        # Write results to sqlmap_results.csv
        save_sqlmap_results(vulnerabilities)
        
        # Append findings to summary.csv
        update_summary(
            scan_type="SQLMap",
            target=target_url,
            vulnerabilities=f"{len(vulnerabilities)} vulnerabilities found",
            details_file=SQLMAP_RESULTS_FILE
        )
        
        print(f"SQLMap results saved to {SQLMAP_RESULTS_FILE}")
        
    except subprocess.CalledProcessError as e:
        print(f"SQLMap encountered an error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def save_sqlmap_results(vulnerabilities):
    """Save SQLMap scan results to a CSV file."""
    try:
        with open(SQLMAP_RESULTS_FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=vulnerabilities[0].keys())
            writer.writeheader()
            writer.writerows(vulnerabilities)
        print("SQLMap scan results successfully written.")
    except Exception as e:
        print(f"Error saving SQLMap results: {e}")
