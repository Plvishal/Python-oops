
from abc import ABC,abstractmethod
"""
Problem-1: Payment System
Goal: Create abstract class Payment with method pay(amount).
Subclasses: CreditCard, UPI, PayPal.
Hint: Use ABC and @abstractmethod.
Focus: Abstract base class + polymorphic call.
"""
print('----------------------Problem-1 Solution---------------------')
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f'Paid {amount} using credit card.')
class UPIPayment(Payment):
    def pay(self, amount):
        print(f'Paid {amount} using UPI.')
credit_card_payment=CreditCardPayment()
credit_card_payment.pay(500)
upi_card_payment=UPIPayment()
upi_card_payment.pay(100)

"""
Problem-2: Vehicle Start System
Goal: Abstract class Vehicle → method start_engine().
Subclasses: Car, Bike, Truck.
Each prints different start messages.
Focus: Enforce same interface for all vehicles.
"""
print('----------------------Problem-2 Solution---------------------')

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self,message):
        pass

class Car(Vehicle):
    def start_engine(self, message):
        print(f'Car start medium noise')
class Bike(Vehicle):
    def start_engine(self, message):
        print(f'Bike start without noise')
class Truck(Vehicle):
    def start_engine(self, message):
        print(f'Truck start loudly')

car=Car()
print(car.start_engine(""))
bike=Bike()
print(bike.start_engine(""))
truck=Truck()
print(truck.start_engine(""))

"""
Problem-3: Notification System
Goal: Abstract class Notification → send(message) method.
Subclasses: EmailNotification, SMSNotification, PushNotification.
Focus: Common interface, different implementations.
"""
print('----------------------Problem-3 Solution---------------------')
class NotificationSystem(ABC):
    @abstractmethod
    def send(self,message):
        pass
class EmailNotification(NotificationSystem):
    def send(self, message):
        print(f'email notification {message}')
class SMSNotification(NotificationSystem):
    def send(self, message):
        print(f'sms notification {message}')
class PushNotification(NotificationSystem):
    def send(self, message):
        print(f'Push notification {message}')

email=EmailNotification()
email.send("This is email alert")
sms=SMSNotification()
sms.send("This sms notification")
push_noti=PushNotification()
push_noti.send("This is push notification")