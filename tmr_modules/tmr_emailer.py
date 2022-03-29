from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(from_email, to_email, subject, html_content, sg_api_key):
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        html_content=html_content
    )
    sg = SendGridAPIClient(sg_api_key)
    response = sg.send(message)
    return response.status_code
