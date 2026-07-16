# ==========================================
#     STUDENT RESUl1T MANAGEMENT SYSTEM
# ==========================================

students = {}


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


def add_student():

    roll = input("\nEnter Roll Number: ")

    if roll in students:
        print("❌ Roll Number already exists.")
        return

    name = input("Enter Student Name: ")

    tel = int(input("Enter Telugu Marks: "))
    hin = int(input("Enter Hindi Marks: "))
    eng = int(input("Enter English Marks: "))
    soc = int(input("Enter Social Marks: "))
    sci = int(input("Enter Science Marks: "))
    mat = int(input("Enter Mathematics Marks: "))

    total = tel + hin + eng + soc + sci + mat
    percentage = total / 6
    grade = calculate_grade(percentage)

    students[roll] = {
        "Name": name,
        "Telugu": tel,
        "Hindi": hin,
        "English": eng,
        "Social": soc,
        "Science": sci,
        "Mathematics": mat,
        "Total": total,
        "Percentage": percentage,
        "Grade": grade
    }

    print("\n✅ Student Result Added Successfully.")


def view_all_students():

    if not students:
        print("\n❌ No student records found.")
        return

    print("\n==================== STUDENT RESULTS ====================")

    for roll, s in students.items():

        print(f"\nRoll Number : {roll}")
        print(f"Name        : {s['Name']}")
        print(f"Total       : {s['Total']}")
        print(f"Percentage  : {s['Percentage']:.2f}%")
        print(f"Grade       : {s['Grade']}")
        print("-" * 50)


def search_student():

    roll = input("\nEnter Roll Number: ")

    if roll not in students:
        print("❌ Student not found.")
        return

    s = students[roll]

    print("\n=============== STUDENT RESULT ===============")
    print(f"Roll Number : {roll}")
    print(f"Name        : {s['Name']}")
    print(f"Telugu      : {s['Telugu']}")
    print(f"Hindi       : {s['Hindi']}")
    print(f"English     : {s['English']}")
    print(f"Social      : {s['Social']}")
    print(f"Science     : {s['Science']}")
    print(f"Mathematics : {s['Mathematics']}")
    print("-" * 45)
    print(f"Total       : {s['Total']}")
    print(f"Percentage  : {s['Percentage']:.2f}%")
    print(f"Grade       : {s['Grade']}")


def topper():

    if not students:
        print("\n❌ No student records available.")
        return

    top_roll = max(students, key=lambda x: students[x]["Percentage"])
    s = students[top_roll]

    print("\n🏆=========== TOPPER DETAILS ===========🏆")
    print(f"Roll Number : {top_roll}")
    print(f"Name        : {s['Name']}")
    print(f"Percentage  : {s['Percentage']:.2f}%")
    print(f"Grade       : {s['Grade']}")


def delete_student():

    roll = input("\nEnter Roll Number to Delete: ")

    if roll in students:
        del students[roll]
        print("✅ Student Record Deleted Successfully.")
    else:
        print("❌ Student not found.")


while True:

    print("\n==========================================")
    print("      STUDENT RESULT MANAGEMENT SYSTEM")
    print("==========================================")

    print("1. Add Student Result")
    print("2. View All Results")
    print("3. Search Student")
    print("4. View Topper")
    print("5. Delete Student Record")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_all_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        topper()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\n🙏 Thank you for using Student Result Management System.")
        break

    else:
        print("❌ Invalid Choice! Please try again.")