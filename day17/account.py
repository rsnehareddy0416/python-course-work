from abc import ABC,abstractmethod
class BankAccount(ABC):
    def checkbalance(self):
        print("You can check your balance")
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class SavingAccount(BankAccount):
    def deposit(self):
        print("2 lakhs per day")
    def withdraw(self):
        print("1 lakh you can withdraw")
class CurrentAccount(BankAccount):
    def deposit(self):
        print("unlimited deposit")
    def withdraw(self):
        print("unlimited withdraw")

class JointAccount(BankAccount):
    def deposit(self):
        print("only those two people can deposit")
    def withdraw(self):
        print("1-2 lakhs per day you can withdraw")
class SalaryAccount(BankAccount):
    def deposit(self):
        print("no limit")
    def withdraw(self):
        print("20K-1 lakh per day")
        
class PensionAccount(BankAccount):
    def deposit(self):
        print("No deposit")
    def withdraw(self):
        print("40K per day")
print("----------abhinandhan-----------")
abhinandan=SavingAccount()
abhinandan.checkbalance()
abhinandan.deposit()
abhinandan.withdraw()

print("----------nandhan-----------")
nandan=CurrentAccount()
nandan.checkbalance()
nandan.deposit()
nandan.withdraw()

print("----------satwik-----------")
satwik=JointAccount()
satwik.checkbalance()
satwik.deposit()
satwik.withdraw()

print("----------abhi-----------")
abhi=SalaryAccount()
abhi.checkbalance()
abhi.deposit()
abhi.withdraw()

print("----------sapnil-----------")
sapnil=PensionAccount()
sapnil.checkbalance()
sapnil.deposit()
sapnil.withdraw()