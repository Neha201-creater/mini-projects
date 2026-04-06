# Initializing an empty dictionary to store student names and their grades
student_grade = {}

# Function to add a new student
def add_student(name, grade):
    student_grade[name] = grade  # Add the student's name as key and grade as value
    print(f"Added {name} with a grade of {grade}")  # Confirm addition

# Function to update an existing student's grade
def update_student(name, grade):
    if name in student_grade:  # Check if the student exists
        student_grade[name] = grade  # Update the grade
        print(f"{name}'s marks have been updated")  # Confirm update
    else:
        print(f"{name} is not found!")  # Show error if student doesn't exist

# Function to delete a student
def delete_student(name):
    if name in student_grade:  # Check if the student exists
        del student_grade[name]  # Remove student from dictionary
        print(f"{name} has been successfully deleted")  # Confirm deletion
    else:
        print(f"{name} is not found!")  # Show error if student doesn't exist

# Function to display all students and their grades
def display_all_students():
    if student_grade:  # Check if the dictionary is not empty
        for name, grade in student_grade.items():  # Loop through all students
            print(f"{name}: {grade}")  # Print each student's name and grade
    else:
        print("No students found/added")  # Inform if there are no students

# Main program function
def main():
    while True:  # Infinite loop to show menu until user chooses to exit
        print('\nStudent Grades Management System')  # Display menu header
        print("1. Add student")  # Option 1
        print("2. Update student")  # Option 2
        print("3. Delete student")  # Option 3
        print("4. View students")  # Option 4
        print("5. Exit")  # Option 5

        # Get user input for menu choice and handle invalid input
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number from 1 to 5.")
            continue  # Restart loop if input is invalid

        if choice == 1:  # Add student
            name = input("Enter student name: ")  # Get student name
            try:
                grade = int(input("Enter student grade: "))  # Get grade
            except ValueError:
                print("Invalid grade! Please enter a number.")  # Handle invalid grade
                continue
            add_student(name, grade)  # Call function to add student

        elif choice == 2:  # Update student
            name = input("Enter student name: ")
            try:
                grade = int(input("Enter student grade: "))
            except ValueError:
                print("Invalid grade! Please enter a number.")
                continue
            update_student(name, grade)  # Call function to update student

        elif choice == 3:  # Delete student
            name = input("Enter student name: ")
            delete_student(name)  # Call function to delete student

        elif choice == 4:  # View all students
            display_all_students()  # Call function to display students

        elif choice == 5:  # Exit program
            print("Closing the program...")
            break  # Exit the while loop

        else:  # Handle invalid menu choice
            print("Invalid choice! Please try again.")

# Start the program
if __name__ == "__main__":
    main()  # Call the main function