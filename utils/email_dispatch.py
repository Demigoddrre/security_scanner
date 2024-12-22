import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from utils.csv_utils import update_summary
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")

def send_email(target_email, subject, content, attachment=None):
    """
    Send a phishing email with optional attachment.

    Args:
        target_email (str): Recipient email address.
        subject (str): Subject line of the email.
        content (str): Body of the email.
        attachment (str, optional): Filepath for attachment. Defaults to None.
    """
    try:
        # Prepare email
        msg = MIMEMultipart()
        msg["From"] = SMTP_USER
        msg["To"] = target_email
        msg["Subject"] = subject

        # Attach email content
        msg.attach(MIMEText(content, "plain"))

        # Attach file if provided
        if attachment:
            try:
                with open(attachment, "rb") as f:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(attachment)}")
                msg.attach(part)
                print(f"Attachment {os.path.basename(attachment)} added.")
            except FileNotFoundError:
                print(f"Attachment {attachment} not found. Skipping.")

        # Connect to SMTP server and send email
        print("Connecting to SMTP server...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(SMTP_USER, target_email, msg.as_string())
            print(f"Email successfully sent to {target_email}.")

        # Update summary
        update_summary(
            scan_type="Email Dispatch",
            target=target_email,
            vulnerabilities="Phishing email sent",
            details_file="N/A" if not attachment else attachment,
        )
        print("Summary updated in summary.csv")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

