def student_database():
    students = {}

    while True:
        print("\n----- Student Database Menu -----")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            roll_no = input("Enter Roll Number: ")

            if roll_no in students:
                print("Student with this roll number already exists!")
            else:
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")

                students[roll_no] = {
                    "Name": name,
                    "Age": age,
                    "City": city
                }

                print("Student added successfully!")

        elif choice == "2":
            roll_no = input("Enter Roll Number to Search: ")

            if roll_no in students:
                print("\nStudent Found")
                print("Roll No :", roll_no)
                print("Name    :", students[roll_no]["Name"])
                print("Age     :", students[roll_no]["Age"])
                print("City    :", students[roll_no]["City"])
            else:
                print("Student not found!")

        elif choice == "3":
            if len(students) == 0:
                print("No student records found.")
            else:
                print("\n----- All Student Records -----")
                for roll_no, details in students.items():
                    print("Roll No :", roll_no)
                    print("Name    :", details["Name"])
                    print("Age     :", details["Age"])
                    print("City    :", details["City"])
                    print("-" * 25)

        elif choice == "4":
            print("Exiting Student Database...")
            break

        else:
            print("Invalid choice! Please try again.")


# Call the function
student_database()