import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_msg(_from, message, subject):
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()

    s.login(os.environ['MY_ADDR'], os.environ['SMTP_PASS'])
    msg = MIMEMultipart()

    msg['From'] = f"Apex Stats - [{_from}]"
    msg['To'] = os.environ['MY_ADDR']
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)
    del msg
