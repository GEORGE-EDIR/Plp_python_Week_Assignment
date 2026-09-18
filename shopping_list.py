# Shopping List Manager

shopping_list = []

while True:
    print("\n--- Shopping List Manager ---")
    print("add / remove / show / done")

    choice = input("Choose an option: ").lower().strip()

    if choice == "add":
        item = input("Enter item to add: ").strip()
        if item:
            shopping_list.append(item)
            print(f"{item} added to your list.")
        else:
            print("Please enter a valid item.")

    elif choice == "remove":
        item = input("Enter item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from your list.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if len(shopping_list) == 0:
            print("Your shopping list is empty.")
        else:
            print("\nYour shopping list:")
            for item in shopping_list:
                print(item)

    elif choice == "done":
        print("Goodbye! Happy shopping!")
        break

    else:
        print("Invalid option. Please choose add, remove, show, or done.")