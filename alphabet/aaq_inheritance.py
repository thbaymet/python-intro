class Animal:

    def __init__(self):
        print('Animal is created')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog is created')


my_dog = Dog()
my_dog.eat()


class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, balance):
        if balance > 0:
            print('Deposit Accepted')
            self.balance += balance

    def withdraw(self, quantity):
        if self.balance >= quantity:
            self.balance -= quantity
            print("Withdrawal accepted")
            return quantity
        else:
            print('Funds unavailable !!')

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"


account = Account('Jane', 30)
print(account)
account.withdraw(20)
print(account)
account.withdraw(12)
print(account)

