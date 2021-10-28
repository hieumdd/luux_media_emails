import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SENDER = "siddhantmehandru.developer@gmail.com"


def compose_message(
    sender: str,
    receiver: str,
    subject: str,
    report: str,
) -> MIMEMultipart:
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receiver
    message.attach(MIMEText("Expand for more", "plain"))
    message.attach(MIMEText(report, "html"))
    return message


def send_email(receivers: list[str], subject: str, report: str) -> list[str]:
    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465,
        context=ssl.create_default_context(),
    ) as server:
        server.login(SENDER, os.getenv("SENDER_PWD"))
        for receiver in receivers:
            server.sendmail(
                SENDER,
                receiver,
                compose_message(SENDER, receiver, subject, report).as_string(),
            )
    return receivers
