class Bank:
    def __init__(self,name,balance,password):
        self.name=name
        self._balance=balance
        self.__password=password
    def get_balance(self):
        return self._balance
    def withdraw(self,amount):
        if amount<=self._balance:
            self._balance-=amount
            return f"Withdraw succesfull!, current balance is {self._balance}"
        else:
            return "Insufficient balance"
b=Bank("Sarma",110000,123)
print(b.name)
print(b.get_balance())
print(b.withdraw(10000))
print(b._Bank__password)
