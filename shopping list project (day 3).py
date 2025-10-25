#Mini project: Shopping List App
shopping_list = []

# --- Load saved list if available ---
try:
    with open("shopping_list.txt", "r") as file:
        lines = file.readlines() #method that reads all lines in a file and returns them as a list of strings
        shopping_list = [line.strip() for line in lines] #list comprehension to remove newline characters
    print("✅ Shopping list loaded successfully!")
except FileNotFoundError:
    print("No saved shopping list found. Starting a new one!")

print("Current items: ", shopping_list)

while True:
    print("\nChoose an action: add / remove / show / clear / search / quit")
    action = input("> ").lower()

    if action == "add":
        added_count = 0
        while True:
            item = input("Enter item to add (type 'done' to stop): ")
            if item == "done":
                break
            else:
                shopping_list.append(item)
                added_count += 1
                print(f"{item} added!")
        print(f"📦 You added {added_count} new items!")
        print(f"You now have {len(shopping_list)} items in your shopping list.")

    elif action == "remove":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed! You now have {len(shopping_list)} items.")
        else:
            print(f"{item} not found in the list.")

    elif action == "show":
        if not shopping_list:
            print("Your shopping list is empty😅.")
        else:
            print("\n🛒 Your shopping list:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")

    elif action == "clear":
        confirmation = input("Are you sure you want to clear the entire list? (yes/no):")
        if confirmation.lower() == "yes":
            shopping_list.clear()
            print("✅ All items cleared! Your shopping list is now empty.")
        else:
            print("❌ Clear action cancelled.")

    elif action == "search":
        item = input("Enter item to search: ")
        if item.lower() in (i.lower() for i in shopping_list):
            print(f"✅ '{item}' is in your shopping list!")
        else:
            print(f"❌ '{item}' is not in your shopping list.")

    elif action == "quit":
        break

    else:
        print("Invalid action. Please choose add, remove, show, or quit.")

# Save the shopping list to a file
with open("shopping_list.txt", "w") as file: #with...as file is a python context manager that automatically opens and closes the file
    for item in shopping_list:
        file.write(f"{item}\n")

print("📝 List saved to shopping_list.txt")
    
    