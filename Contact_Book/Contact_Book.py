# ✅ Build a simple contact book using a dictionary.

contact_book = {}

def get_valid_input():
    while True:
        try:
            user_input = int(input("Please press a number: "))
            if user_input in [1, 2, 3, 4, 5, 6]:
                return user_input   # Valid input
            else:
                print("\nPlease enter a valid number.")
        except ValueError:  # Handle cases where the user doesn't enter a number
            print("\nPlease enter a valid input.")

def get_valid_name():
    valid_name = input("\nEnter contact name: ")
    return valid_name.strip().casefold()   # for case-insensitive matching

def get_valid_number():
    while True:
        valid_number = input("Enter contact number: ")
        if valid_number.isdigit():
            return int(valid_number)
        print("Invalid input. Please enter a valid number.")


while True:

    print("\nWhat do you want to do?")
    # Display options
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Exit the program")

    user_choice = get_valid_input()

    if user_choice == 1:
        # 1️⃣ Add a contact
        # Ask for the contact name and phone number.
        # Store them in the dictionary.
        # If the contact already exists, warn the user.
        name = get_valid_name()
        if name in contact_book:
            print("This contact already exits.")
            print("Do you still want to update the contact?")
            choice = input("Press y/n: ")
            if choice.lower() == "y":
                user_choice = 4
            else:
                continue  # Go back to the menu
        else:
            contact_book[name] = get_valid_number()
            print("Contact added successfully!")

    elif user_choice == 2:
        # 2️⃣ View all contacts
        # Print all contacts in a formatted way.
        print("\nContacts:")
        # for contact in contact_book:
        #     print(f"{contact} : {contact_book[contact]}")
        if contact_book:
            for name, number in contact_book.items():
                print(f"{name.capitalize()} : {number}")
        else:
            print("No contacts found.")

    elif user_choice == 3:
        # 3️⃣ Search for a contact
        # Ask for the contact name.
        # If found, display the phone number.
        # If not found, show "Contact not found."
        name = get_valid_name()
        if name in contact_book:
            print(f"{name.capitalize()} : {contact_book[name]}")
        else:
            print("Contact not found.")

    elif user_choice == 4:
        # 4️⃣ Update a contact
        # Ask for the contact name.
        # If it exists, allow the user to enter a new phone number.
        # If not, show "Contact not found."
        name = get_valid_name()
        if name in contact_book:
            contact_book[name] = get_valid_number()
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    elif user_choice == 5:
        # 5️⃣ Delete a contact
        # Ask for the contact name.
        # If it exists, delete it using del dictionary[key].
        # If not found, show "Contact not found."
        name = get_valid_name()
        if name in contact_book:
            del contact_book[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    else:
        # 6️⃣ Exit the program
        # Use break to stop the loop when the user chooses to exit.
        print("Exiting program. Goodbye!")
        break