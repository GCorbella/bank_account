class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Client(User):
    def __init__(self, name, surname, account_n, balance):
        super().__init__(name, surname)
        self.account_n = account_n
        self.balance = balance

    def print_client(self):
        print("*" * 50)
        print(f"Welcome to Python Bank, {self.name} {self.surname}.")
        print(f"Your current account is {self.account_n}, with a balance of {self.balance}€.")

    def deposit(self):
        self.balance = self.balance + int(input("How many money do you want to deposit in your account? "))
        print("Thank you for your contribution.")

    def retire(self):
        c_retire = int(input("How many money do you want to retire from your account? "))
        if self.balance - c_retire < 0:
            print("Your account doesn't have enough funds for this operation.")
        else:
            self.balance = self.balance - c_retire
            print("Thank you for trusting Python Bank.")

def create_client():
    client.name = input("Please enter your name: ")
    client.surname = input("Please enter your surname: ")
    client.account_n = int(input("Please, enter your birth year and the last four numbers of your ID: "))
    client.balance = int(input("Do you want to make an initial deposit? Enter the quantity below. If not, enter 0: "))
    print("Your client in Python Bank have been succesfuly created. Thank you!")

def home():
    selection = ""
    while selection != "3":
        client.print_client()
        selection = input("""
        What do you want to do?
        [1] Deposit.
        [2] Withdrawal.
        [3] Exit.
        
        """)
        if selection == "1":
            client.deposit()
        elif selection == "2":
            client.retire()
        elif selection == "3":
            print("*" * 50)
            print("Thank you for working with Python Bank.")
            working = False

client = Client("name", "surname", "account_n", "balance")

print("-" * 50)
print("WELCOME TO PYTHON BANK!")
print("-" * 50)
create_client()
home()