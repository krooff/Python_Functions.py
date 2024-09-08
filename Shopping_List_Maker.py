#Task 1: Function to add items to a list
def add_item(shopping_list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"'{item}' has been added to your list.")

#Task 2: Function to remove items from list
def remove_item(shopping_list):
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your list.")
    else:
        print(f"'{item}' is not in your list.")

#Task 3: Function to print the entire list
def print_list(shopping_list):
    if shopping_list:
        print("\nYour shopping list:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
        print()
    else:
        print("\nYour shopping list is empty.\n")

# Task Undefined(All of them?): Using Funtions in while loop
def shopping_list_program():
    shopping_list = []
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. View the list")
        print("4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            print_list(shopping_list)
        elif choice == '4':
            print("Quiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
    
