def add_contact():
    name = input("Enter Name: ")

    phone = input("Enter Phone Number: ")

    if len(phone) != 10 or not phone.isdigit():
        print("Invalid Mobile Number! Enter exactly 10 digits.")
        return

    file = open("contacts.txt", "a")
    file.write(name + " - " + phone + "\n")
    file.close()

    print("Contact saved successfully!")


def view_contacts():
    file = open("contacts.txt", "r")
    data = file.read()
    file.close()

    if data:
        print("\n--- CONTACTS ---")
        print(data)
    else:
        print("No contacts found!")


while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")