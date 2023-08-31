options = """

[1] - Deposit
[2] - Withdraw
[3] - Statement
[0] - Exit

-> """

balance = 0
limit = 500
statement = ""
withdraw_times = 0
WITHDRAW_LIMIT = 3

while True:

    option = input(options)

    if option == "1":
        value = float(input("Please enter Deposit amount: "))

        if value > 0:
            balance += value
            statement += f"Deposited amount: ${value:.2f}\n"

        else:
            print("Error! Operation failed: Informed value is invalid.")
    
    elif option == "2":
        value = float(input("Please enter Withdraw amount: "))

        exceeded_balance = value > balance

        exceeded_limit = value > limit

        exceeded_withdraw_limit = withdraw_times >= WITHDRAW_LIMIT

        if exceeded_balance:
            print("Error! Operation failed: Balance is insuficient.")
        
        elif exceeded_limit:
            print("Error! Operation failed: Withdraw amount exceeds limit.")
        
        elif exceeded_withdraw_limit:
            print("Error! Operation failed: Withdraw limit reached.")
        
        elif value > 0:
            balance -= value
            statement == f"Withdraw: $ {value:.2f}\n"
            withdraw_times += 1
        
        else:
            print("Error! Operation failed: Informed value is invalid.")

    elif option == "3":
        print("\n#################### BANK STATEMENT ####################")
        print("No operations were made." if not statement else statement)
        print(f"\nBalance: $ {balance:.2f}")
        print("\n########################################################")
    
    elif option == "0":
        break

    else:
        print("Error! Invalid operation, please select valid option.")
