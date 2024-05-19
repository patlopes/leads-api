import time
from infrastructure.config import Config

class Email:
    def __init__(self):
        self.config = Config()
        
    def send(self, to, subject, body):
        print(f"Sending email to {to} with subject {subject} and body {body}")
        time.sleep(1)
        print("Email sent!")