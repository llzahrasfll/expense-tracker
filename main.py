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

def print_menu():
    print("===Expense Tracker=== \n 1) Add expense \n 2) Show expense \n 3) Filter by category \n 4) Delete expense \n 5) Summery by category \n 6) Exit")

def add_expense(expenses):
    amount = float(input("Amount:"))
    category = input("Category:")
    description =input("Description:")
    expense = {"amount": amount, "category": category, "description": description}
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added")

def show_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
    else:
        total = 0
        for i,expense in enumerate(expenses, start= 1):
            print(f"{i}. {expense['amount']} | {expense['category']} | {expense['description']}")
            total += expense['amount']
        print('Total:', total)

def filter_expenses(expenses):
    wanted = input("Category:")
    found = False
    for expense in expenses:
        if expense["category"].lower() == wanted.lower():
            print(f"{expense['amount']} | {expense['category']} | {expense['description']}")
            found = True
    if not found:
        print('Nothing found.')

def delete_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
    else:
        for i,expense in enumerate(expenses, start= 1):
            print(f"{i}. {expense['amount']} | {expense['category']} | {expense['description']}")
        number = int(input("Number to delete:"))
        if 1<= number <= len(expenses):
            expenses.pop(number -1)
            save_expenses(expenses)
            print("Deleted!")
        else:
            print("Invalid number.")

def summary_by_category(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    totals ={}
    for expense in expenses:
        cat = expense["category"].lower()
        totals[cat] = totals.get(cat, 0) + expense["amount"]
    for cat, total in totals.items():
        print(f"{cat}: {total}")
 
def main():
    expenses = load_expenses()
    while True:
        print_menu()
        choice = input("Your choice:")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            filter_expenses(expenses)
        elif choice == "4":
            delete_expenses(expenses)
        elif choice == "5":
            summary_by_category(expenses)
        elif choice == "6":
            print('Goodbye!')
            break
        else:
            print("Invalid choice, try again.")
    
main()