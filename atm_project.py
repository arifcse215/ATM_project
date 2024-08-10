class ATM:
    def __init__(self):
        print("\n----Welcome To ATM----\n")
        self.pin = "1234"
        self.mobile = '01521515530'
        self.amount = 1000.00
        self.count = 1


    def varify_acount(self):
        pword = input("Enter your 4-digit PIN or type 'exit' to quit: ")
        if self.pin == pword:
            self.display()
        elif pword.lower() == 'exit':
            return 0
        elif self.count < 2:
            print("Invalid PIN")
            self.count += 1
            self.varify_acount()
        elif self.count == 2:
            print("Its your last time")
            self.count += 1
            self.varify_acount()
        else:
            self.count = 1
            return 0

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: $"))
        if amount <= self.amount:
            self.amount -= amount
            print(f"${format(amount, '.2f')} has been withdrawn. Remain balance is: ${format(self.amount, '.2f')}\n")
            self.display()

    def diposit(self):
        amount = float(input("Enter amount to diposit: $"))
        self.amount += amount
        print(f'${format(amount, ".2f")} has been diposited. Update balance: ${format(self.amount, ".2f")}\n')
        self.display()

    def changePin(self):
        pin = input("Enter old PIN: ")
        if pin == self.pin:
            newPin = input("Enter new 4-digit PIN: ")
            if len(newPin) == 4 and newPin.isdigit():
                self.pin = newPin
                print("PIN changed successfully!")
                self.varify_acount()
            else:
                print("Invalid PIN format. PIN must be 4-digit number.\nTry again!!!")
                self.changePin()
        else:
            print("Invalid PIN. Try agin!!!")

    def display(self):
        print("1. Check Balance.")
        print("2. Withdraw Money.")
        print("3. Diposit Money.")
        print("4. Change PIN.")
        print("5. Exit\n")
        self.get()

    def get(self):
        manu = input("What should like to do? Enter number: ")
        match manu:
            case "5":
                print("\nThank you for using ATM. Goodbye!\n")
                return 0
            case "1":
                print(f'Your corrent balance is: ${format(self.amount, ".2f")}')
                print()
                self.display()
            case "2":
                self.withdraw()
            case "3":
                self.diposit()
            case "4":
                self.changePin()


person = ATM()
person.varify_acount()
