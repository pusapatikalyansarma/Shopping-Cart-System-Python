# ==========================================
#      LIBRARY MANAGEMENT SYSTEM
# ==========================================

library = {}


def add_book():

    book_id = input("\nEnter Book ID: ")

    if book_id in library:
        print("❌ Book ID already exists.")
        return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    library[book_id] = {
        "Title": title,
        "Author": author,
        "Status": "Available"
    }

    print("\n✅ Book Added Successfully.")


def view_books():

    if not library:
        print("\n📚 No books available.")
        return

    print("\n================ LIBRARY BOOKS ================")

    for book_id, book in library.items():

        print(f"\nBook ID : {book_id}")
        print(f"Title   : {book['Title']}")
        print(f"Author  : {book['Author']}")
        print(f"Status  : {book['Status']}")
        print("-" * 45)


def search_book():

    book_id = input("\nEnter Book ID: ")

    if book_id not in library:
        print("❌ Book Not Found.")
        return

    book = library[book_id]

    print("\n========== BOOK DETAILS ==========")
    print(f"Book ID : {book_id}")
    print(f"Title   : {book['Title']}")
    print(f"Author  : {book['Author']}")
    print(f"Status  : {book['Status']}")


def issue_book():

    book_id = input("\nEnter Book ID to Issue: ")

    if book_id not in library:
        print("❌ Book Not Found.")
        return

    if library[book_id]["Status"] == "Issued":
        print("❌ Book is already issued.")
    else:
        library[book_id]["Status"] = "Issued"
        print("✅ Book Issued Successfully.")


def return_book():

    book_id = input("\nEnter Book ID to Return: ")

    if book_id not in library:
        print("❌ Book Not Found.")
        return

    if library[book_id]["Status"] == "Available":
        print("❌ Book is already available.")
    else:
        library[book_id]["Status"] = "Available"
        print("✅ Book Returned Successfully.")


def delete_book():

    book_id = input("\nEnter Book ID to Delete: ")

    if book_id in library:
        del library[book_id]
        print("✅ Book Deleted Successfully.")
    else:
        print("❌ Book Not Found.")


while True:

    print("\n========================================")
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("========================================")

    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        delete_book()

    elif choice == "7":
        print("\n📚 Thank you for using Library Management System.")
        break

    else:
        print("❌ Invalid Choice. Please try again.")