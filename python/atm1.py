accounts = {
    "1234": 100,
    "5678": 250,
    "4321": 500
}

while True:
    print("\n===== Welcome to the ATM =====")
    pin = input("Enter your PIN: ")

    if pin in accounts:
        print(f"\nWelcome! Account {pin} recognized.")

        while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Logout")

            choice = input("Please select an option (1-4): ")

            if choice == '1':
                print(f"Your current balance is: ${accounts[pin]}")

            elif choice == '2':
                amount = float(input("Enter amount to deposit: $"))
                if amount > 0:
                    accounts[pin] += amount
                    print(f"${amount} deposited successfully.")
                    print(f"New balance: ${accounts[pin]}")
                else:
                    print("Invalid amount. Please enter a positive number.")

            elif choice == '3':
                amount = float(input("Enter amount to withdraw: $"))
                if 0 < amount <= accounts[pin]:
                    accounts[pin] -= amount
                    print(f"${amount} withdrawn successfully.")
                    print(f"Remaining balance: ${accounts[pin]}")
                else:
                    print("Invalid amount or insufficient funds.")

            elif choice == '4':
                print("Logging out...\n")
                break

            else:
                print("Invalid selection. Please choose a valid option.")
    else:
        print("Invalid PIN. Try again.")
