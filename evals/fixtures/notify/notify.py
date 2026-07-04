"""Send alerts to the channels the team actually watches."""

import json
import urllib.request


def send_slack(webhook_url, message):
    """Post message to a Slack incoming webhook."""
    body = json.dumps({"text": message}).encode()
    req = urllib.request.Request(
        webhook_url, data=body, headers={"Content-Type": "application/json"}
    )
    urllib.request.urlopen(req)


def send_email(smtp_host, recipient, message):
    """Send message as a plain-text email via local SMTP."""
    import smtplib
    from email.message import EmailMessage

    msg = EmailMessage()
    msg["To"] = recipient
    msg["Subject"] = "Alert"
    msg.set_content(message)
    with smtplib.SMTP(smtp_host) as smtp:
        smtp.send_message(msg)
