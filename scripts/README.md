# Scripts Directory

This directory contains scripts for simulating various types of cybersecurity attacks for **educational purposes only**. Each script is accompanied by a corresponding reversal script and detailed documentation to ensure responsible usage.

## **Table of Contents**
1. [Overview](#overview)
2. [Script Descriptions](#script-descriptions)
    - [Ransomware Simulation](#ransomware-simulation)
    - [Keylogger Simulation](#keylogger-simulation)
    - [Trojan Simulation](#trojan-simulation)
    - [Spyware Simulation](#spyware-simulation)
    - [Worm Simulation](#worm-simulation)
    - [Denial of Service (DoS) Simulation](#denial-of-service-dos-simulation)
3. [Usage](#usage)
4. [Important Notes](#important-notes)
5. [Disclaimer](#disclaimer)

## **Overview**
The `scripts/` folder contains Python scripts that simulate different types of cyberattacks. These simulations are designed to demonstrate the behavior and potential impact of various attack methods in a controlled and ethical environment.

Each script has a corresponding reversal script located in the `utils/reversal_scripts/` directory to reverse any simulated damage.

## **Script Descriptions**

### **Ransomware Simulation**
- **Filename:** `ransomware_simulation.py`
- **Purpose:** Simulates file encryption by appending a `.locked` extension to files in a specified directory.
- **Reversal Script:** `reversal_scripts/ransomware_reversal.py`
- **Impact:** Demonstrates how ransomware affects file accessibility.

### **Keylogger Simulation**
- **Filename:** `keylogger_simulation.py`
- **Purpose:** Captures and logs keystrokes to simulate keylogging activity.
- **Reversal Script:** `reversal_scripts/keylogger_reversal.py`
- **Impact:** Highlights potential risks to sensitive information, such as passwords.

### **Trojan Simulation**
- **Filename:** `trojan_simulation.py`
- **Purpose:** Simulates creating and exfiltrating mock sensitive data.
- **Reversal Script:** `reversal_scripts/trojan_reversal.py`
- **Impact:** Demonstrates how trojans can compromise system integrity.

### **Spyware Simulation**
- **Filename:** `spyware_simulation.py`
- **Purpose:** Simulates monitoring user activity and collecting mock data.
- **Reversal Script:** `reversal_scripts/spyware_reversal.py`
- **Impact:** Illustrates privacy risks associated with spyware.

### **Worm Simulation**
- **Filename:** `worm_simulation.py`
- **Purpose:** Simulates replicating files across directories to demonstrate worm-like behavior.
- **Reversal Script:** `reversal_scripts/worm_reversal.py`
- **Impact:** Highlights how worms can consume resources and spread.

### **Denial of Service (DoS) Simulation**
- **Filename:** `dos_simulation.py`
- **Purpose:** Simulates sending a flood of requests to a mock server.
- **Reversal Script:** `reversal_scripts/dos_reversal.py`
- **Impact:** Demonstrates how DoS attacks disrupt system availability.

## **Usage**

1. **Simulating an Attack:**
   - Navigate to the project directory.
   - Run the desired script from the `scripts/` folder:
     ```bash
     python scripts/<script_name>.py
     ```

2. **Reversing the Simulation:**
   - Navigate to the `utils/reversal_scripts/` directory.
   - Run the corresponding reversal script:
     ```bash
     python utils/reversal_scripts/<reversal_script_name>.py
     ```

3. **Logging:**
   - All activities, including simulation details and reversal logs, are saved in:
     - `outputs/malware_logs.csv`
     - `outputs/phishing_logs.csv`

## **Important Notes**
- Always run these scripts in a sandboxed environment or virtual machine.
- Ensure all necessary dependencies are installed as listed in the `requirements.txt` file.
- Use only for educational purposes or within controlled lab environments.

## **Disclaimer**
This project is for **educational purposes only**. The authors do not condone or support the use of these scripts for malicious purposes. Misuse of these scripts may violate local, state, or federal laws, and users are solely responsible for adhering to applicable regulations.
