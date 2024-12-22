### **Updated README.md**

---

# **Network Security Tool**

This Python-based network security tool facilitates **network scanning**, **traffic analysis**, **database vulnerability assessments**, and **phishing campaigns** using utilities like Nmap, Pyshark, SQLMap, and OpenAI-powered social engineering. The tool provides a command-line interface (CLI) for streamlined user interaction and exports all results to CSV files for further analysis.

---

## **Features**
1. **Intelligence Gathering**
   - **Network Scanning**: Use Nmap to scan for open ports and services.
   - **Traffic Analysis**: Monitor and analyze packets in real-time using Pyshark.

2. **Database Vulnerability Assessment**
   - Identify vulnerabilities using SQLMap and export results for review.

3. **Phishing Campaigns**
   - **Email Generation**: Create AI-generated phishing emails using OpenAI.
   - **Malware Handling**: Select and attach predefined malware scripts (e.g., ransomware, keylogger simulations).
   - **Automated Dispatch**: Send phishing emails with optional attachments.

4. **Malware Reversal Toolkit**
   - Reverse the effects of simulated malware attacks using dedicated reversal scripts.

5. **Centralized Logging**
   - Save all activities in detailed CSV logs:
     - `summary.csv`: High-level overview of all operations.
     - `nmap_results.csv`, `traffic_results.csv`, `sqlmap_results.csv`: Specific operation logs.
     - `phishing_logs.csv`: Phishing campaign details.
     - `malware_logs.csv`: Malware attachment details.
     - `reversal_logs.csv`: Logs for malware reversal operations.

---

## **Project Structure**
```
network_security_tool/
├── main.py                      # Entry point for the tool
├── menu.py                      # Main menu system
├── utils/
│   ├── nmap_utils.py            # Functions for Nmap scans
│   ├── pyshark_utils.py         # Functions for traffic analysis
│   ├── sqlmap_utils.py          # SQLMap database vulnerability scanning
│   ├── phishing_utils.py        # Phishing and email automation functions
│   ├── malware_utils.py         # Handle malware script selection and logging
│   ├── csv_utils.py             # CSV operations for logging results
│   ├── reversal_scripts/        # Scripts to reverse malware effects
│       ├── ransomware_reversal.py
│       ├── keylogger_reversal.py
│       ├── worm_reversal.py
│       ├── trojan_reversal.py
├── outputs/                     # Logs and scan results
│   ├── summary.csv              # High-level summary of all operations
│   ├── nmap_results.csv         # Detailed Nmap scan results
│   ├── traffic_results.csv      # Detailed traffic capture logs
│   ├── sqlmap_results.csv       # SQLMap scan results
│   ├── phishing_logs.csv        # Logs for phishing campaigns
│   ├── malware_logs.csv         # Logs for malware scripts sent
│   ├── reversal_logs.csv        # Logs for malware reversal operations
├── scripts/                     # Predefined malware scripts
│   ├── ransomware_sim.py
│   ├── trojan_sim.py
│   ├── keylogger_sim.py
│   ├── worm_sim.py
├── requirements.txt             # Dependencies
├── .env                         # Environment variables for sensitive data
```

---

## **Prerequisites**
1. **Install Required Tools and Libraries**
   - **Nmap**: Install from [Nmap.org](https://nmap.org/).
   - **SQLMap**: Install from [sqlmap.org](https://sqlmap.org/).
   - **Wireshark/TShark**: Install from [Wireshark.org](https://www.wireshark.org/).

   **Python Libraries:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables**
   - Create a `.env` file for sensitive data (e.g., OpenAI API key, SMTP credentials):
     ```
     OPENAI_API_KEY=your_openai_key
     SMTP_SERVER=smtp.example.com
     SMTP_PORT=587
     SMTP_USER=your_email@example.com
     SMTP_PASS=your_password
     ```

---

## **Usage**
1. **Run the Tool**
   Navigate to the project directory and execute:
   ```bash
   python main.py
   ```

2. **Menu Options**
   - **1. Scan Network (Nmap)**: Perform network scans and export results.
   - **2. Listen to Traffic (Pyshark)**: Capture and analyze packets.
   - **3. Scan Database (SQLMap)**: Assess database vulnerabilities.
   - **4. Phishing Campaigns**: Generate and send phishing emails with optional malware attachments.
   - **5. Reversal Toolkit**: Reverse the effects of malware simulations.
   - **6. Exit**: Exit the tool.

3. **Phishing Sub-Menu**
   - **1. Generate Phishing Email**: Create AI-generated phishing content.
   - **2. Select Malware Attachment**: Choose a malware script from predefined options.
   - **3. Send Email**: Dispatch the phishing email to a target.
   - **4. Back to Main Menu**: Return to the main menu.

4. **Reversal Toolkit Sub-Menu**
   - **1. Reverse Ransomware**: Decrypt files affected by ransomware.
   - **2. Remove Keylogger**: Clean keylogger infections.
   - **3. Clean Worm Infection**: Remove worm infections.
   - **4. Stop Trojan Service**: Terminate malicious trojan services.
   - **5. Back to Main Menu**: Return to the main menu.

---

## **Output Files**
All results are saved in the `outputs/` directory:
- `summary.csv`: Overview of all operations.
- `nmap_results.csv`: Results of network scans.
- `traffic_results.csv`: Captured traffic details.
- `sqlmap_results.csv`: Database vulnerability assessments.
- `phishing_logs.csv`: Details of phishing campaigns.
- `malware_logs.csv`: Logs of malware attachments.
- `reversal_logs.csv`: Logs of malware reversal operations.

---

## **Using the Application with or Without a VPN**
### **VPN and Scanning**
- **Effect on Scanning**: VPNs route traffic through their servers, masking your IP.
- **Best Practices**:
  - Disconnect VPN for local scans.
  - Use VPN IP for external scans.

### **Finding Your IP Address**
#### **Public IP**
- **PowerShell**:
  ```powershell
  (Invoke-WebRequest -uri "http://ifconfig.me/ip").Content
  ```
- **Online**: Use [WhatIsMyIP](https://www.whatismyip.com/).

#### **Private IP**
- **PowerShell**:
  ```powershell
  ipconfig
  ```
- Look for **IPv4 Address** under the relevant adapter.

---

## **Ethical Usage**
This tool is designed strictly for **authorized environments and ethical purposes**. Misuse of this tool for malicious purposes is illegal and violates ethical guidelines.

---

## **Future Enhancements**
- **Encryption**: Encrypt all output CSV files for added security.
- **GUI Development**: Add a graphical user interface for easier interaction.
- **Automated Reporting**: Integrate email-based reporting for completed operations.

---

### **Disclaimer**
By using this tool, you agree to use it responsibly in authorized testing environments only. Any misuse is solely the user's responsibility.
