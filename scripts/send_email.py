import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_question_email(question_text: str, day_num: int):
    """
    Sends the generated SQL question via email.
    """
    email_user = os.getenv("EMAIL_USER")
    email_password = os.getenv("EMAIL_PASSWORD")
    email_to = os.getenv("EMAIL_TO")
    
    if not all([email_user, email_password, email_to]):
        logging.warning("Email credentials not fully configured. Skipping email notification.")
        return
        
    subject = f"New SQL Interview Question Added - Day {day_num:03d}"
    current_date = datetime.now().strftime("%Y-%m-%d")
    file_name = f"day-{day_num:03d}.md"
    
    body = f"""Hello,

A new SQL Interview Question has been successfully generated for {current_date}.

📁 File Name: {file_name}
📅 Date Generated: {current_date}
🔗 Repository Link: https://github.com/arsudsandesh97/Daily-SQL

Here is the question:
=========================================================

{question_text}

=========================================================
Keep up the great work!
SQL-Interview-365 Bot
"""
    
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        logging.info("Connecting to SMTP server...")
        # Assuming Gmail SMTP as per instructions
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)
        
        logging.info("Sending email...")
        server.send_message(msg)
        server.quit()
        logging.info("Email sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
