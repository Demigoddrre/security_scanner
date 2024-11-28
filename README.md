# Network Security Tool

This Python-based network security tool facilitates network scanning, traffic analysis, and database vulnerability assessments by integrating utilities such as Nmap, Pyshark, and SQLMap. It offers a command-line interface for streamlined user interaction.

## Project Structure

```
network_security_tool/
├── main.py
├── menu.py
├── utils/
│   ├── nmap_utils.py
│   ├── pyshark_utils.py
│   ├── sqlmap_utils.py
│   ├── csv_utils.py
├── outputs/
│   ├── summary.csv
│   ├── nmap_results.csv
│   ├── traffic_results.csv
│   ├── sqlmap_results.csv
```

- **main.py**: Entry point initializing the application and handling user interactions.
- **menu.py**: Manages the command-line menu system, presenting options and invoking corresponding functions.
- **utils/**: Contains utility modules:
  - **nmap_utils.py**: Functions for network scanning using Nmap.
  - **pyshark_utils.py**: Functions for traffic analysis using Pyshark.
  - **sqlmap_utils.py**: Functions for database vulnerability scanning using SQLMap.
  - **csv_utils.py**: Functions for handling CSV operations, including writing scan results.
- **outputs/**: Directory for storing output files:
  - **summary.csv**: Central summary of all scans performed.
  - **nmap_results.csv**: Detailed results from Nmap scans.
  - **traffic_results.csv**: Detailed results from traffic analysis.
  - **sqlmap_results.csv**: Detailed results from SQLMap scans.

## Prerequisites

Ensure the following tools and libraries are installed:

- **Python 3.x**: Programming language for the tool.
- **pip**: Python package installer.
- **Nmap**: Network scanning tool.
- **SQLMap**: Automated SQL injection tool.
- **Wireshark/TShark**: Network protocol analyzer required for Pyshark.

Install the required Python libraries:

```bash
pip install pyshark
```

## Usage

Navigate to the project directory and run the main script:

```bash
python3 main.py
```

Follow the on-screen menu to select the desired operation:

1. **Scan Network**: Performs a network scan using Nmap.
2. **Listen to Traffic**: Captures and analyzes network traffic using Pyshark.
3. **Scan Database**: Conducts a database vulnerability scan using SQLMap.
4. **Exit**: Exits the application.

## Output Files

Results from scans are saved in the `outputs/` directory:

- **summary.csv**: High-level overview of all scans performed, including scan type, target, vulnerabilities found, and date.
- **nmap_results.csv**: Detailed results from Nmap scans.
- **traffic_results.csv**: Detailed results from traffic analysis.
- **sqlmap_results.csv**: Detailed results from SQLMap scans.

## Next Steps: Docker and Terraform Integration

To enhance deployment and scalability, the following steps are planned:

1. **Dockerization**:
   - **Objective**: Containerize the application to ensure consistent environments across different systems.
   - **Benefits**:
     - Simplifies deployment and dependency management.
     - Facilitates scalability and isolation.
   - **Plan**:
     - Create a `Dockerfile` defining the application's environment and dependencies.
     - Build a Docker image and test the containerized application.
     - Publish the Docker image to a container registry for easy access.

2. **Infrastructure Provisioning with Terraform**:
   - **Objective**: Automate the provisioning of infrastructure required for the application, such as virtual machines, networks, and storage.
   - **Benefits**:
     - Ensures consistent and repeatable deployments.
     - Simplifies infrastructure management and scaling.
   - **Plan**:
     - Define infrastructure components using Terraform configuration files.
     - Integrate the Dockerized application into the provisioned infrastructure.
     - Test the deployment to ensure functionality and performance.

By implementing Docker and Terraform, the network security tool will achieve greater flexibility, scalability, and ease of deployment, facilitating more efficient testing and development workflows. 