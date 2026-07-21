rooms = {
    101: ["Single", 1500, "Available"],
    102: ["Double", 2500, "Available"],
    103: ["Deluxe", 3500, "Available"],
    104: ["Suite", 5000, "Available"]
}

bookings = {}


def show_rooms():
    print("\n--- ROOM DETAILS ---")
    for no, data in rooms.items():
        print(no, data[0], "Rs." + str(data[1]), data[2])


def book_room():
    show_rooms()
    no = int(input("\nEnter Room Number: "))

    if no not in rooms:
        print("Room not found!")
    elif rooms[no][2] == "Booked":
        print("Room already booked!")
    else:
        name = input("Enter Customer Name: ")
        days = int(input("Enter Number of Days: "))

        rooms[no][2] = "Booked"
        bookings[no] = [name, days]

        print("Room booked successfully!")


def checkout():
    no = int(input("\nEnter Room Number: "))

    if no not in bookings:
        print("No booking found!")
    else:
        name, days = bookings[no]
        bill = rooms[no][1] * days

        print("\nCustomer:", name)
        print("Room:", no)
        print("Days:", days)
        print("Total Bill: Rs.", bill)

        rooms[no][2] = "Available"
        del bookings[no]

        print("Checkout successful!")


while True:
    print("\n===== HOTEL MANAGEMENT =====")
    print("1. View Rooms")
    print("2. Book Room")
    print("3. Checkout")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        show_rooms()
    elif choice == "2":
        book_room()
    elif choice == "3":
        checkout()
    elif choice == "4":
        print("Thank you! Visit Again.")
        break
    else:
        print("Invalid Choice!")