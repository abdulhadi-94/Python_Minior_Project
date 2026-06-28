class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []

    # Add marks with validation
    def add_mark(self, mark):
        if 0 <= mark <= 100:
            self.marks_list.append(mark)
            print("Mark added successfully.")
        else:
            raise ValueError("Marks should be between 0 and 100.")

    # Calculate average
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)

    # Display student information
    def display_info(self):
        print("\n----- Student Details -----")
        print("Name      :", self.name)
        print("Roll No   :", self.roll_no)
        print("Marks     :", self.marks_list)
        print("Average   :", self.get_average())


# ---------------- Main Program ----------------

try:
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    student = Student(name, roll_no)

    n = int(input("How many marks do you want to enter? "))

    for i in range(n):
        try:
            mark = float(input(f"Enter mark {i + 1}: "))
            student.add_mark(mark)
        except ValueError as e:
            print("Error:", e)

    student.display_info()

except ValueError:
    print("Invalid input! Please enter correct values.")

except Exception as e:
    print("An unexpected error occurred:", e)