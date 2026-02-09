import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

SENDER = os.getenv("EMAIL_USER")
PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER = os.getenv("TO_EMAIL")


def send_email(subject, body ):
    if not SENDER or not PASSWORD :
        print("Email credentials missing in .env file. Skipping email notification.")
        return  
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER, PASSWORD)

            message = f"Subject: {subject}\n\n{body}"
            
            server.sendmail(SENDER, RECEIVER, message)
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")        