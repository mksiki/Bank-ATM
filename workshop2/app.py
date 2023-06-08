
from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


"""
Task 2: Register the user's name and PIN. Create variable balance  
"""

print("          === Automated Teller Machine ===          ")

name = input("Username: ")
pin = input("PIN: ")
balance = format(0, '.2f')
print(f"Congratulations {name}! Your account has been created "
      f"with a balance of ${balance}.\n")

# LOGIN

while True:
    login_name = input("Login Name: ")
    login_pin = input("Pin: ")

    if name == login_name and pin == login_pin:
        print("Login Successful")
        break
    print("Invalid Credentials")

# Display ATM menu and responds to user choice

while True:
    atm_menu(name)
    option = input("Choose an option: ")

    if option == '1':
        account.show_balance(balance)
    elif option == '2':
        balance = account.deposit(balance)
    elif option == '3':
        balance = account.withdraw(balance)
    elif option == '4':
        account.logout(name)
        quit()
    else:
        print("You did not select one of the options...")
        print()
