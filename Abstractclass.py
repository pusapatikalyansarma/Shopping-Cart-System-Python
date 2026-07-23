from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def transaction_status(self):
        pass

    @abstractmethod
    def payment_mode(self):
        pass


class UPI(Payment):

    def pay(self, amount):
        print("Paid Rs.", amount, "using UPI")

    def refund(self, amount):
        print("Refunded Rs.", amount, "through UPI")

    def check_balance(self):
        print("UPI balance checked")

    def transaction_status(self):
        print("UPI transaction successful")

    def payment_mode(self):
        print("Payment Mode: UPI")


class Card(Payment):

    def pay(self, amount):
        print("Paid Rs.", amount, "using Card")

    def refund(self, amount):
        print("Refunded Rs.", amount, "through Card")

    def check_balance(self):
        print("Card balance checked")

    def transaction_status(self):
        print("Card transaction successful")

    def payment_mode(self):
        print("Payment Mode: Card")


upi = UPI()
card = Card()

upi.pay(500)
upi.refund(100)
upi.check_balance()
upi.transaction_status()
upi.payment_mode()

print()

card.pay(1000)
card.refund(200)
card.check_balance()
card.transaction_status()
card.payment_mode()