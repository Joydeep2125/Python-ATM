# for stopping program execution for some time
import time

print("Welcome To Trusted Bank")

print("\nPlease insert Your CARD")

# for card processing
time.sleep(3)

password = (1234)

# taking atm pin from user
pin = int(input("Enter your atm pin : "))

# user account balance
balance = 5000

# name of the user
name = "Joydeep"

# checking pin is valid or not
if pin == password:

    while True:
        print("Welcome to your account",name)

        # Showing  info to user

        print(""" 
			1 == Balance
			2 == Withdraw 
			3 == Deposit 
			4 == Exit
			"""
              )

        try:
            # taking an option from user
            option = int(input("Please enter your choice : "))
        except:
            print("Please enter a valid option")


        if option == 1:
            if balance <= 5000:
                print("Low balance")
                print("Your current balance is Rs.",balance)
            else:
                print("Your current balance is Rs.",balance)

        elif option == 2:
            withdraw_amount = int(input("Please enter withdraw amount : "))
            if withdraw_amount <= balance:
                balance = balance - withdraw_amount
                print("Rs.",withdraw_amount, "is debited from your account")
                print("Your updated balance is Rs.",balance)
            else:
                print("Insufficient Balance")

        if option == 3:
            deposit_amount = int(input("Please enter deposit amount : "))
            balance = balance + deposit_amount
            print("Rs.",deposit_amount,"is credited to your account")
            print("Your updated balance is Rs.",balance)

        if option == 4:
            print("Thank you :) Have a nice day")
            print("Please remove your card")
            break


else:
    print("Wrong pin")
    print("Please try again")


