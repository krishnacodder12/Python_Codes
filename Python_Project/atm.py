class ATMInterface:
    def __init__(self, pin, account_number, initial_balance):
        self.__pin = pin
        self.__account_number = account_number
        self.__bank_balance = initial_balance

    def check_balance(self):
        return f"Account Balance: ${self.__bank_balance}"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__bank_balance:
            self.__bank_balance -= amount
            return f"Withdrawal successful. Remaining Balance: ${self.__bank_balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def change_pin(self, new_pin):
        self.__pin = new_pin
        return "PIN changed successfully."

    def get_account_number(self):
        return f"Account Number: {self.__account_number}"

if __name__ == "__main__":
    my_atm = ATMInterface(pin="1234", account_number="9876543210", initial_balance=1000.0)

    print(my_atm.check_balance())
    print(my_atm.withdraw(500))
    print(my_atm.check_balance())
    print(my_atm.change_pin("5678"))
    print(my_atm.get_account_number())
