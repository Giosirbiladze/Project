print("Please Enter your name:")
name = input()
print("Please Enter your lastname:")
lastname = input()
print("Please Enter your phonenumber:")
phonenumber = input()
print("Please Enter information about your card:")
cardinformation = input()

def show_balance(balance):
    print("*************")
    print(f"your balance is lari(balance:2f)")
    print("*************")


def deposit():
    print("*************")
    amount = float(input("Enter an amount to be depositede:"))
    print("*************")
    if amount < 0:
        print("*************")
        print("That's not valid amount")
        print("*************")
        return 0 
    else:
        return amount

def withdraw(balance):
    print("*************")
    amount = float("Enter amount to be withdrawn:")
    print("*************")

    if amount > balance:
        print("*************")
        print("insuffcient funds")
        print("*************")
    elif amount < 0:
        print("*************")
        print("Amount must be greater than 0")
        print("*************")
        return 0 
    else:
        return amount
def main():
    balance = 0
    is_running = True

    while is_running:
        print("*************")
        print(" GIO's BANK ")
        print("*************")
        print("1.show balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")
        print("*************")
        choice = input("Enter your choice (1-4):")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("*************")
            print("that is not a valid choice")
            print("*************")

    print("*************")
    print("thank you")
    print("*************")

    if __name__ == '__main__':
     main()
