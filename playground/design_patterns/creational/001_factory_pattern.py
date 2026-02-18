'''
### POINTS TO REMEMBER

1. Factory pattern encapsulates object creation logic and returns objects based on input without exposing instantiation details.
2. Constructor creates a specific class directly but Factory decides which class to create based on input.

When to Use Factory Pattern (IDENTIFY FAST) -
✅ You have multiple related classes
✅ Which class to instantiate depends on input/config
✅ You see repeated if-else creation logic
✅ You want to hide object creation complexity

Advantages -
✅ Cleaner code
✅ Easy to maintain and extend
✅ Loose coupling between client and concrete classes
✅ Centralized object creation logic

Disadvantages -
✅ Factory becomes huge if too many types of notifications are added
✅ Adding new notification types requires modifying the factory class, which can violate the Open/Closed Principle
'''


from abc import ABC, abstractmethod

# Create an interface (base class) for notifications
class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass

# Create concrete implementations of the Notification interface
class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Sending email notification: {message}")
    
class SMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Sending SMS notification: {message}")

class MMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Sending MMS notification: {message}")

# Create a factory class to generate notifications based on the type
class NotificationFactory:    
    @staticmethod
    def create_notification(notification_type: str) -> Notification:
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "mms":
            return MMSNotification()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")


# Client usage
if __name__ == "__main__":
    factory = NotificationFactory()
    email_notification = factory.create_notification("email")
    email_notification.send("Hello via Email!")

