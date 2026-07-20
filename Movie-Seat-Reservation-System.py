# ================================
#    MOVIE SEAT RESERVATION
# ================================

seats = [
    ["A1", "A2", "A3", "A4", "A5"],
    ["B1", "B2", "B3", "B4", "B5"],
    ["C1", "C2", "C3", "C4", "C5"]
]


def show_seats():
    print("\n========== SEAT LAYOUT ==========")

    for row in seats:
        print(" | ".join(row))


def book_seat():
    seat = input("\nEnter Seat Number: ").upper()

    for row in seats:
        if seat in row:
            index = row.index(seat)
            row[index] = "XX"
            print("✅ Seat Booked Successfully.")
            return

    print("❌ Seat Not Found or Already Booked.")


def cancel_seat():
    seat = input("\nEnter Seat Number to Cancel: ").upper()

    for row in seats:
        if "XX" in row:
            index = row.index("XX")
            row[index] = seat
            print("✅ Booking Cancelled.")
            return

    print("❌ No booked seat found.")


while True:

    print("\n==============================")
    print("   MOVIE SEAT RESERVATION")
    print("==============================")

    print("1. View Seats")
    print("2. Book Seat")
    print("3. Cancel Booking")
    print("4. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        show_seats()

    elif choice == "2":
        book_seat()

    elif choice == "3":
        cancel_seat()

    elif choice == "4":
        print("\n🎬 Thank you! Enjoy your movie.")
        break

    else:
        print("❌ Invalid Choice.")