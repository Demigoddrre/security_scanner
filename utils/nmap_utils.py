import subprocess
import csv
from utils.csv_utils import update_summary

def scan_network():
    target = input("Enter the target IP or network range (e.g., 192.168.1.0/24): ")
    details_file = "outputs/nmap_results.csv"

    command = ["nmap", "-sV", target, "-oN", "outputs/nmap_raw.txt"]
    try:
        subprocess.run(command, check=True)
        print("Nmap scan completed. Parsing results...")

        # Example CSV writing (replace with real parsing logic)
        with open(details_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Target", "Port", "Service", "Version", "Status"])
            writer.writerow([target, "22", "SSH", "OpenSSH 8.0", "Open"])
            writer.writerow([target, "80", "HTTP", "Apache 2.4", "Open"])

        vulnerabilities = "2 open ports"
        print(f"Results saved to {details_file}")
        update_summary("Nmap", target, vulnerabilities, details_file)
    except Exception as e:
        print(f"Error running Nmap: {e}")
