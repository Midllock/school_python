from abc import ABC, abstractmethod
from typing import Dict

class Message(ABC):
    @abstractmethod
    def get_content(self) -> str:
        pass

class TextMessage(Message):
    def __init__(self, sender: str, receiver: str, message: str):
        self.sender = sender
        self.receiver = receiver
        self.message = message

    def get_content(self) -> str:
        return f"\nOdesílatel: {self.sender}\nPříjemce: {self.receiver}\nZpráva: {self.message}\n"

class EmailMessage(Message):
    def __init__(self, sender: str, receiver: str, subject: str, message: str):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.message = message

    def get_content(self) -> str:
        return f"Odesílatel: {self.sender}\nPříjemce {self.receiver}\nPředmět: {self.subject}\n\n{self.message}\n"

class PushNotification(Message):
    def __init__(self, title: str, message: str, timestamp: str):
        self.title = title
        self.message = message
        self.timestamp = timestamp

    def get_content(self) -> str:
        return f"{{\n\t\"Nadpis\": \"{self.title}\",\n\t\"Zpráva\": \"{self.message}\",\n\t\"Čas odeslání\": \"{self.timestamp}\"\n}}"

class MessageFactory:
    def __init__(self):
        self.message_types: Dict[str, type] = {
            "text": TextMessage,
            "email": EmailMessage,
            "push": PushNotification
        }

    def create_message(self, message_type: str, **kwargs) -> Message:
        if message_type not in self.message_types:
            raise ValueError(f"Neplatný typ zprávy: {message_type}")
        return self.message_types[message_type](**kwargs)

# Testování
factory = MessageFactory()

text_message = factory.create_message("text", sender="+420123456789", receiver="+420987654321", message="Dobrý den, Vaše objednávka byla právě odeslána. Děkujeme za nákup!")
print(text_message.get_content())

email_message = factory.create_message("email", sender="odesilatel@example.com", receiver="prijemce@example.com", subject="Předmět zprávy", message="Dobrý den, toto je ukázkový text e-mailové zprávy. S pozdravem, [Vaše jméno]")
print(email_message.get_content())

push_notification = factory.create_message("push", title="Nová zpráva", message="Máš novou notifikaci! Klikni pro více informací.", timestamp="2025-03-14T12:34:56Z")
print(push_notification.get_content())