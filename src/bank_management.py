import sys

class Atm:
    def __init__(self):
        self.__pin = 0
        self.__balance = 0
        self.user_menu()

    def set_pin(self, new_pin):
        try:
            if len(str(new_pin)) == 4:
                self._Atm__pin = new_pin
                return "New Pin Successfully Set...!"
            else:
                return "Pin length has to be 4 characters."
        except:
            return "Pin is not a valid integer"

    def get_pin(self):
        return self._Atm__pin

    def get_balance(self):
        return self._Atm__balance

    def deposit_amount(self, deposit_amount):
        self._Atm__balance += deposit_amount
        return "Amount Deposited Successfully...!"

    def amount_withdraw(self, withdrawal_amount):
        if self._Atm__balance >= withdrawal_amount:
            self._Atm__balance -= withdrawal_amount
            return "Amount Deducted Successfully"
        else:
            return "Your Account Doesn't have sufficient Balance..!"

    def user_menu(self):
        print("Welcome to ATM Banking.\nPlease select options from below Menu")
        user_input = int(input("1. Check Balance\n2. Deposit Amount\n3. Withdraw Amount\n4. Reset Pin\n5. Exit Services"))
        if user_input >=1 and user_input <=4:
            if user_input == 1:
                print(self.get_balance())
            elif user_input == 2:
                print(self.deposit_amount(float(input("Enter the Amount you wish to deposit"))))
            elif user_input == 3:
                print(self.amount_withdraw(float(input("Enter the Amount you wish to withdraw"))))
            elif user_input == 4:
                print(self.set_pin(int(input("Please Enter the New Pin You wish to Enter"))))
            self.user_menu()

        elif user_input == 5:
            print("Thank you for using our services. Have a Great Day")
            sys.exit(0)

        else:
            print("Please Enter a Valid Input. Redirecting you to home Menu.")
            self.user_menu()

#Definig the Object for the ATM Class
sbi_user = Atm()
#user_pin = sbi_user.get_pin()