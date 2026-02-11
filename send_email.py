import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_html_email(sender_email, sender_password, recipient_email, subject, html_content):
    """
    Send an HTML email using Gmail's SMTP server.
    
    Args:
        sender_email (str): Your Gmail address
        sender_password (str): Your Gmail app password (not regular password)
        recipient_email (str): Recipient's email address
        subject (str): Email subject
        html_content (str): HTML content of the email
    """
    
    # Create message container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    # Create the HTML part
    html_part = MIMEText(html_content, 'html')
    
    # Attach HTML content to message
    msg.attach(html_part)
    
    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Enable security
        
        # Login to your account
        server.login(sender_email, sender_password)
        
        # Send email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        
        print(f"Email sent successfully to {recipient_email}!")
        
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        
    finally:
        server.quit()


import os
from dotenv import load_dotenv
from datetime import datetime


if __name__ == "__main__":

    load_dotenv()
    
    # Get credentials from environment variables
    SENDER_EMAIL = os.environ.get('SENDER_EMAIL')
    SENDER_PASSWORD = os.environ.get('SENDER_PASSWORD')
    RECIPIENT_EMAIL = os.environ.get('RECIPIENT_EMAIL')
    
    # Validate that all required environment variables are set
    if not all([SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL]):
        print("Error: Missing required environment variables!")
        print("Please set: SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL")
        exit(1)
    
    # Set email subject based on day of the week
    day_of_week = datetime.now().strftime('%A')
    
    subject_map = {
        'Monday': 'Midwalls Monday',
        'Tuesday': 'Traceable Tuesday',
        'Wednesday': 'Wild Wednesday',
        'Thursday': 'Teutuli Thursday',
        'Friday': 'Flag Fredag!',
    }
    
    SUBJECT = subject_map.get(day_of_week, 'Daily Teutuli')
    
    # Read HTML content from file
    try:
        with open('output.html', 'r', encoding='utf-8') as file:
            HTML_CONTENT = file.read()
    except FileNotFoundError:
        print("Error: output.html file not found!")
        print("Please create an output.html file in the same directory.")
        exit(1)
    except Exception as e:
        print(f"Error reading output.html: {str(e)}")
        exit(1)
    
    # Send the email
    send_html_email(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, SUBJECT, HTML_CONTENT)
