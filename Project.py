# Import necessary libraries
import datetime
import json
import os

# Define a class to track expenses
class ExpenseTracker:
    # Initialize the tracker with a fun
    def __init__(self, data_file='expenses.json'):
        self.data_file = data_file
        self.expenses = self.load_expenses()

    # Load expenses from the data file fun
    def load_expenses(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        else:
            return []

    # Save expenses to the data file fun
    def save_expenses(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.expenses, f)

    # Add a new expense fun
    def add_expense(self):
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")

        expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }

        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added successfully!")

    # View all expenses fun
    def view_expenses(self):
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")

    # Delete an expense fun
    def delete_expense(self):
        self.view_expenses()
        index = int(input("Enter expense number to delete: ")) - 1
        if index >= 0 and index < len(self.expenses):
            del self.expenses[index]
            self.save_expenses()
            print("Expense deleted successfully!")
        else:
            print("Invalid expense number.")

    # Calculate total expenses fun
    def calculate_total(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"Total expenses: {total}")

    # Filter expenses by category fun
    def filter_by_category(self):
        category = input("Enter category: ")
        filtered_expenses = [expense for expense in self.expenses if expense['category'] == category]
        # Display filtered expenses
        for expense in filtered_expenses:
            print(f"Date: {expense['date']}, Amount: {expense['amount']}, Description: {expense['description']}")

# Main function
def main():
    # Create an ExpenseTracker instance
    tracker = ExpenseTracker()

    # Loop until user chooses to exit
    while True:
        print("\nDaily Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Calculate Total")
        print("5. Filter by Category")
        print("6. Exit")

        # Get user choice
        choice = input("Enter your choice: ")

        # Handle user choice
        if choice == '1':
            tracker.add_expense()
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.delete_expense()
        elif choice == '4':
            tracker.calculate_total()
        elif choice == '5':
            tracker.filter_by_category()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()