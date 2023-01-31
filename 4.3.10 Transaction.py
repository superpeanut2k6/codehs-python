initial_balance = 1000
user_choice = input("Would you like to make a deposit or would you like to withdrawal?Type deposit for a deposit and withdrawal for a withdrawal")


if user_choice == "withdrawal":
    withdraw_ammount = int(input("How much money would you like to withdraw?"))
    if withdraw_ammount >1000:
        print("You cannot have a negative balance")
    else:
        initial_balance = initial_balance - withdraw_ammount
    print("Final balance:", str(initial_balance))
elif user_choice == "deposit":
    deposit_ammount = int(input("How much money would you like to deposit?"))
    initial_balance = initial_balance + deposit_ammount
    print("Final balance:", str(initial_balance))
else:
    print("Invalid transaction")