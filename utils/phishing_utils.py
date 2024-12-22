import openai
import csv
import os
from utils.csv_utils import update_summary

def generate_phishing_email():
    """
    Generates phishing email content using the OpenAI API and saves results to phishing_logs.csv.
    """
    openai.api_key = os.getenv("OPENAI_API_KEY")
    logs_file = "outputs/phishing_logs.csv"

    try:
        # User inputs for email generation
        company_name = input("Enter the target company name (e.g., ExampleCorp): ")
        email_context = input("Enter the email context (e.g., password reset, billing issue): ")
        recipient_name = input("Enter the recipient's name (optional): ")

        # Construct prompt for OpenAI API
        prompt = f"""
        Generate a phishing email with the following details:
        - Target Company: {company_name}
        - Email Context: {email_context}
        - Recipient Name: {recipient_name or "User"}
        The email should appear professional, include a call to action, and simulate a real-world scenario.
        """

        print("Generating phishing email content...")
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=250,
            temperature=0.7
        )
        email_content = response["choices"][0]["text"].strip()
        print("\nGenerated Email:\n")
        print(email_content)

        # Save generated email to phishing_logs.csv
        with open(logs_file, 'a', newline='') as f:
            writer = csv.writer(f)
            # Create headers if file doesn't exist
            if f.tell() == 0:
                writer.writerow(["Company Name", "Email Context", "Recipient Name", "Generated Email"])
            writer.writerow([company_name, email_context, recipient_name, email_content])
        print(f"Phishing email saved to {logs_file}")

        # Update summary
        summary_message = f"Phishing email generated for {company_name} with context '{email_context}'"
        update_summary("Phishing Email Generation", company_name, summary_message, logs_file)
        print("Summary updated in summary.csv")

    except Exception as e:
        print(f"Error generating phishing email: {e}")
