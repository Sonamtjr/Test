# Initialize empty lists and dictionaries to store student information
students_list = []
students_dict = {}

# Function to add a student
def add_student():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grade = input("Enter student's grade: ")
    
    students_list.append(name)
    students_dict[name] = {'age': age, 'grade': grade}
    
    print(f"Student {name} added successfully.")
    print_students()

# Function to print all students
def print_students():
    print("\nCurrent Students:")
    for name, info in students_dict.items():
        print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")
    print()

# Function to search for a student by name
def search_student():
    name = input("Enter the student's name to search: ")
    if name in students_dict:
        info = students_dict[name]
        print(f"Found student: Name: {name}, Age: {info['age']}, Grade: {info['grade']}")
    else:
        print(f"Student {name} not found.")

# Function to remove a student by name
def remove_student():
    name = input("Enter the student's name to remove: ")
    if name in students_dict:
        students_list.remove(name)
        del students_dict[name]
        print(f"Student {name} removed successfully.")
        print_students()
    else:
        print(f"Student {name} not found.")

# Main function to run the Student Information Management System
def main():
    while True:
        print("1. Add student")
        print("2. Search student")
        print("3. Remove student")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            remove_student()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
