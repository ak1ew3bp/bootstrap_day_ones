balance = 1000

while True:
    print("\nWelcome to the ATM!")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Please select an option (1-4): ")
    
    if choice == '1':
        print(f"Your current balance is: ${balance}")
    
    elif choice == '2':
        amount = float(input("Enter amount to deposit: $"))
        if amount > 0:
            balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid amount. Please enter a positive number.")
    
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: $"))
        if 0 < amount <= balance:
            balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Invalid amount. Please check your balance and try again.")
    
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    
    else:
        print("Invalid selection. Please choose a valid option.")