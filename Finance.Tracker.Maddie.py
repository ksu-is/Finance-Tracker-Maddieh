import csv
from datetime import datetime


FILE_NAME = 'finance.tracker.maddie'


def initialize_file():
    try:
        with open(FILE_NAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Type', 'Amount', 'Description'])
    except FileExistsError:
        pass


def add_transaction(transaction_type, amount, description):
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime(''), transaction_type, amount, description])


def view_balance():
    balance = 0.0
    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Type'] == 'Income':
                balance += float(row['Amount'])
            elif row['Type'] == 'Expense':
                balance -= float(row['Amount'])
    return balance


def generate_summary():
    summary = {'Income': 0.0, 'Expense': 0.0}
    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Type'] == 'Income':
                summary['Income'] += float(row['Amount'])
            elif row['Type'] == 'Expense':
                summary['Expense'] += float(row['Amount'])
    return summary


def main():
    initialize_file()
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. Generate Summary")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            description = input("Enter description: ")
            add_transaction('Income', amount, description)
            print("Income added successfully.")
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            description = input("Enter description: ")
            add_transaction('Expense', amount, description)
            print("Expense added successfully.")
        elif choice == '3':
            balance = view_balance()
            print(f"Current Balance: ${balance:.2f}")
        elif choice == '4':
            summary = generate_summary()
            print(f"Total Income: ${summary['Income']:.2f}")
            print(f"Total Expense: ${summary['Expense']:.2f}")
        elif choice == '5':
            print("Exiting the tracker. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
