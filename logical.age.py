def check_discount_eligibility():
    age = int(input("Please enter your age: "))

    student_status = input("Are you a student? (yes/no): ").strip().lower()

    if age <= 12:
        print("You are eligible for a discount.")
    elif 13 <= age <= 18 and student_status == 'yes':
        print("You are eligible for a discount.")
    else:
        print("You are not eligible for a discount.")

check_discount_eligibility()
