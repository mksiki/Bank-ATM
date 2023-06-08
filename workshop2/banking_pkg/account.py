def show_balance(balance):
    print(f"Your balance is: ${balance}")
    input("Press Enter to continue...")
    


def deposit(balance):
    amount = float(input("Deposit Amount: "))
    balance = float(balance)
    balance += amount
    balance = format(balance, '.2f')
    return balance


def withdraw(balance):
    amount = float(input("Withdraw Amount: "))
    balance = float(balance)

    if balance < amount:
        print(f"You dont have the sufficient funds, your balance is {balance}")

    else:
        balance -= amount
        balance = format(balance, '.2f')
        return balance


def logout(name):
    print(f"Goodbye {name}")

