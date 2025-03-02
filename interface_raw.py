from abc import ABC, abstractmethod 

class NotificationSender(ABC):

  @abstractmethod
  def send_notification(self, message: str) -> None: pass

class EmailNotificationSender(NotificationSender):

  def send_notification(self, message: str) -> None:
    print(f"Email sent with message: {message}")

class SMSNotificationSender(NotificationSender):

  def send_notification(self, message: str) -> None:
    print(f"SMS sent with message: {message}")  

class Notificator: 
  def __init__(self, notification_sender: NotificationSender) -> None:
    self.__notification_sender = notification_sender
  
  def send_notification(self, message: str) -> None:
    self.__notification_sender.send_notification(message)

obj = Notificator(SMSNotificationSender())
obj.send_notification("Hello, how are you?")