from infrastructure.email import Email
from infrastructure.config import Config

class EmailService:
    def __init__(self):
        self.email_client = Email()
        self.config = Config()

    def send_email(self, to, subject, body):
        self.email_client.send(to, subject, body)

    def send_welcome_email(self, to):
        self.send_email(to, "Welcome!", "Welcome to our platform! We're excited to have you here.")

    def send_notify_admin_email(self):
        admin_email = self.config.DEFAULT_EMAIL_ADMIN
        self.send_email(admin_email, "New Lead!", "A new lead has been created. Check the dashboard for more details.")