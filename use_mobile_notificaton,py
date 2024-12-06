from twilio.rest import Client

class NotificationService:
    def __init__(self, account_sid, auth_token, from_number):
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number

    def send_sms(self, to_number, message):
        try:
            message = self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=to_number
            )
            print(f"SMS sent successfully: {message.sid}")
        except Exception as e:
            print(f"Failed to send SMS: {e}")

if __name__ == "__main__":
    ACCOUNT_SID = "your_account_sid"
    AUTH_TOKEN = "your_auth_token"
    FROM_NUMBER = "your_twilio_number"
    TO_NUMBER = "recipient_phone_number"

    notifier = NotificationService(ACCOUNT_SID, AUTH_TOKEN, FROM_NUMBER)
    notifier.send_sms(TO_NUMBER, "Alert! High temperature detected in Smart Toilet.")
