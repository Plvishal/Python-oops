"""
Problem-1: Bank Account Balance
Goal: Create a class BankAccount with private balance __balance.
Add methods: deposit(), withdraw(), and get_balance().
Hint: Use __balance to make it private.
Focus: Private variables, getters & setters.
"""
class BankAccount():
        def __init__(self,name,balance):
                self.name=name
                self.__balance=balance
        def deposit(self,amount):
                self.__balance+=amount
        def withdraw(self,amount):
                if amount >=0:
                    self.__balance-=amount
                else:
                       print("Amount always be positive")
        def get__balance(self):
                return self.__balance
        def set__balance(self,amount):
                if amount >=0:
                    self.__balance -=amount
                else:
                     print("Amount always be positive")
        
account=BankAccount('Vishal Pal',10000)
print(f" Get Account Before depoit {account.get__balance()}")
account.deposit(15000)
print(f" Get Account After depoit {account.get__balance()}")
account.set__balance(1000)
print(f" Get Account After set balance {account.get__balance()}")

"""
Problem-2: Student Report Card
Goal: Make a class Student that hides marks using a private variable.
Allow adding marks via method, but not directly.
Hint: Add add_marks() and show_result() methods.
Focus: Data hiding & controlled access.
"""
print("-----------------------------Problem-2 Solution-----------------------")
class Students ():
    def __init__(self,name,marks):
              self.name=name
              self.__marks=marks
    def add_marks(self,marks):
           self.__marks+=marks
    def show_result(self):
         match self.__marks:
            case marks if marks < 33:
                print("Fail")
            case 33:
                print("Just pass")
            case marks if 34 <= marks < 60:
                print("Good Marks")
            case marks if 60 <= marks < 80:
                print("Very Good")
            case marks if marks >= 80:
                print("Excellent!")
            case _:
                print("Invalid marks")
student=Students("Vishal pal",30)
student.show_result()
student.add_marks(3)
student.show_result()
student.add_marks(30)
student.show_result()
              

""""
Problem-3: Password Protectio
Goal: Create a UserAccount class with a private password.
Add methods set_password() and check_password().
Hint: Don’t print password directly; use a verification method.
Focus: Secure attribute management.
"""
print("-----------------------------Problem-3 Solution-----------------------")

class UserAccount():
    def __init__(self,password):
            self.__password=password
    def set_password(self,password):
          self.__password=password
    def check__password(self):
          return self.__password
          
useraccount=UserAccount('vishal123')
print(f'Before setting the password {useraccount.check__password()}')
useraccount.set_password("vishal@12")
print(f'After setting the password {useraccount.check__password()}')


