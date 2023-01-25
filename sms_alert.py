import os
import requests
import datetime as dt
from twilio.rest import Client

SID = os.environ.get("SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
SEND_NUMBER = os.environ.get("SEND_NUMBER")


class Alert:
    def __init__(self, receive_number: str, message: str):
        self.client = Client(SID, AUTH_TOKEN)
        self.send_number = SEND_NUMBER
        self.receive_number = receive_number
        self.message = message

    def create_message(self, user_message: str):
        self.message = user_message

    def send_alert(self):
        alert = self.client.messages \
            .create(body=self.message,
                    from_=self.send_number,
                    to=self.receive_number
                    )
        print(alert.status)
