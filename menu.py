from utils.nmap_utils import scan_network
from utils.pyshark_utils import listen_to_traffic
from utils.sqlmap_utils import scan_database

def main_menu():
    while True:
        print("\n=== Security Toolkit ===")
        print("1. Scan Network (Nmap)")
        print("2. Listen to Traffic (Pyshark)")
        print("3. Scan Database (SQLMap)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            scan_network()
        elif choice == "2":
            listen_to_traffic()
        elif choice == "3":
            scan_database()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
