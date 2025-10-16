#Midterm Pt2
class Account:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.") 
        return self.balance   

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough funds.")
            return None
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}.")
        return self.balance


class SavingsAccount(Account):
    def __init__(self, accountNumber, balance, interestRate):
        super().__init__(accountNumber, balance)
        self.interestRate = interestRate

    def applyInterest(self):
        interest = self.balance * self.interestRate / 100
        self.balance += interest
        print(f"Applied interest of {interest}. New balance is {self.balance}.")

class CheckingAccount(Account):
    def __init__(self, accountNumber, balance, overdraftLimit):
        super().__init__(accountNumber, balance)
        self.overdraftLimit = overdraftLimit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraftLimit:
            print("Not enough funds.")
            return self.balance
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")


#Accounts 
accounts = [
    SavingsAccount("S29820231", 2600, 0.5),
    CheckingAccount("C393244029", 2435, 100),
    SavingsAccount("SA59384857", 39722, 1.4),
    CheckingAccount("C53567706",780, 100)
      ] 


