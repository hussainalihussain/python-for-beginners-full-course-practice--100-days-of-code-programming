class Bank:
    def __init__(self, bankName, totalAmount):
        self.bankName = bankName
        self.totalAmount = totalAmount
    
    def __str__(self):
        return f"{self.bankName} have {self.totalAmount}"
    
    def __add__(self, other):
        return Bank("Person", self.totalAmount + other.totalAmount)

bank1 = Bank("Meezan", 6000)
bank2 = Bank("Faysal", 1000)

print(bank1)
print(bank2)

print(bank1 + bank2)