import pyshark
import csv
from utils.csv_utils import update_summary

def listen_to_traffic():
    interface = input("Enter the network interface to listen on (e.g., eth0, wlan0): ")
    details_file = "outputs/traffic_results.csv"

    try:
        print(f"Listening on {interface}... Capturing 10 packets.")
        capture = pyshark.LiveCapture(interface=interface)
        packets = []

        for packet in capture.sniff_continuously(packet_count=10):
            packets.append({
                "Timestamp": packet.sniff_time,
                "Source IP": packet.ip.src if hasattr(packet, 'ip') else "N/A",
                "Destination IP": packet.ip.dst if hasattr(packet, 'ip') else "N/A",
                "Protocol": packet.highest_layer,
                "Length": packet.length,
                "Info": str(packet)
            })

        with open(details_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=packets[0].keys())
            writer.writeheader()
            writer.writerows(packets)

        vulnerabilities = f"{len(packets)} packets captured"
        print(f"Traffic results saved to {details_file}")
        update_summary("Traffic", interface, vulnerabilities, details_file)
    except Exception as e:
        print(f"Error capturing traffic: {e}")
