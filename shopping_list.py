import os
shopping_list = []
print("Welcome to ShoppingList app 🛒")
################# function : add_item #################
def add_item():
    print("do you want to go back to the main menu? enter q ")
    while True:
        new_item = input("please enter new item name: ").strip()
        if new_item == "q":
            break
        elif new_item in shopping_list:
            print(f"{new_item} is already in your list!")
        else:
            shopping_list.append(new_item)
            print(f"{new_item} successfully added to your list.")


############### function : remove_item #################
def remove_item():
    print("do you want to go back to the main menu? enter q ")
    while True:
        item_to_remove = input("please enter item name to remove: ").strip()
        if item_to_remove == "q":
            break
        elif item_to_remove not in shopping_list:
            print(f"{item_to_remove} is not in your shopping list!")
        else:
            shopping_list.remove(item_to_remove)
            print(f"{item_to_remove} successfully removed.")


############### function : view_list ###################
def view_list():
    print("do you want to go back to the main menu? enter q ")
    if shopping_list:
        print("Your Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
        print("*******************")
    else:
        print("Your shopping list is empty!")


############## function : exit ########################
def exit_function():
    print("thank you for using shopping list app. goodbye :)")

############# function : save_to_file #################
def save_to_file():
    with open("shopping_list.txt", "w") as file:
        for item in shopping_list:
            file.write(item + "\n")
    print("Shopping list saved to 'shopping_list.txt'")

############# function : load_from_file ###############
def load_from_file():
    if os.path.exists("shopping_list.txt"):
        with open("shopping_list.txt", "r") as file:
            global shopping_list
            shopping_list = [line.strip() for line in file.readlines()]
        print("Shopping list loaded from 'shopping_list.txt'")
    else:
        print("No saved shopping list found.")
############## main program ###########################
while True:
    try:
        user_choosed_option = int(
            input("1. Add item\n2. Remove item\n3. View list\n4. Save to file\n5. Load from file\n6. Exit\nchoose what do you want to do: "))

        if user_choosed_option == 1:
            add_item()
        elif user_choosed_option == 2:
            remove_item()
        elif user_choosed_option == 3:
            view_list()
        elif user_choosed_option == 4:
            save_to_file()
            view_list()
        elif user_choosed_option == 5:
            load_from_file()
            view_list()
        elif user_choosed_option == 6:
            exit_function()
            break
        else:
            print("please enter a valid number!")
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 6.")
