expenses = []
while True:
    print("===Expense Tracker=== \n 1) Add expense \n 2) Show expense \n 3) Exit")
    choice = input("Your choice:")
    if choice == "1":
        amount = float(input("Amount:"))
        category = input("Category:")
        description =input("Description:")
        expense = {"amount": amount, "category": category, "description": description}
        expenses.append(expense)
        print("Expense added")
        print(expenses)

    elif choice == "2":
        print('Coming soon!')
    elif choice == "3":
        print('Goodbye!')
        break
    else:
        print("Invalid choice, try again.")