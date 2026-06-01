students = []

# ---------- LOAD DATA ----------
def load_data():
    try:
        file = open("students.txt", "r")
        for line in file:
            parts = line.strip().split(",")
            students.append({
                "id": parts[0],
                "name": parts[1],
                "marks": int(parts[2])
            })
        file.close()
    except:
        print("No previous data found.")

# ---------- SAVE DATA ----------
def save_data():
    file = open("students.txt", "w")
    for s in students:
        file.write(s["id"] + "," + s["name"] + "," + str(s["marks"]) + "\n")
    file.close()

# ---------- FUNCTIONS ----------
def add_student():
    sid = input("Enter ID: ")
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    students.append({"id": sid, "name": name, "marks": marks})
    save_data()
    print("Student added successfully!")

def view_students():
    if len(students) == 0:
        print("No students found")
        return

    print("\n--- STUDENT LIST ---")
    for s in students:
        print(s)

def search_student():
    sid = input("Enter ID: ")
    for s in students:
        if s["id"] == sid:
            print("Found:", s)
            return
    print("Not found")

def delete_student():
    sid = input("Enter ID: ")
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            save_data()
            print("Deleted successfully")
            return
    print("Not found")

def topper_student():
    if not students:
        print("No data")
        return

    top = students[0]
    for s in students:
        if s["marks"] > top["marks"]:
            top = s

    print("Topper:", top)

def report():
    if not students:
        print("No data")
        return

    total = 0
    pass_count = 0
    fail_count = 0

    for s in students:
        total += s["marks"]
        if s["marks"] >= 40:
            pass_count += 1
        else:
            fail_count += 1

    print("\n--- REPORT ---")
    print("Total Students:", len(students))
    print("Average Marks:", total / len(students))
    print("Passed:", pass_count)
    print("Failed:", fail_count)

# ---------- MENU ----------
def menu():
    print("\n===== STUDENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Topper Student")
    print("6. Report")
    print("7. Exit")

# ---------- MAIN ----------
load_data()

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        topper_student()
    elif choice == "6":
        report()
    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Invalid choice")