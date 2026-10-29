import json
filename = 'expenses.json' 
def load_expenses():
    try:
        with open(filename,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with  open(filename, "w") as f:
        json.dump(expenses, f, indent= 2)

expenses = load_expenses()

while True:
    print("===Expense Tracker=== \n 1) Add expense \n 2) Show expense \n 3) Exit")
    choice = input("Your choice:")
    if choice == "1":
        amount = float(input("Amount:"))
        category = input("Category:")
        description =input("Description:")
        expense = {"amount": amount, "category": category, "description": description}
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added")

    elif choice == "2":
        if not expenses:
            print("No expenses yet.")
        else:
            total = 0
            for i,expense in enumerate(expenses, start= 1):
                print(f"{i}. {expense['amount']} | {expense['category']} | {expense['description']}")
                total += expense['amount']
            print('Total:', total)

    elif choice == "3":
        print('Goodbye!')
        break
    else:
        print("Invalid choice, try again.")
