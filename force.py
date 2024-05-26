print("Newton's  Law of Motion")
print("Force is the product of mass into acceleration")

#Determine the missing value
print("select the missing value")
print("1. Mass (m)")
print("2. Acceleration (a)")
print("3. Force (f)")
missing_value_choice =input("Enterthe option number for the missing value:\n ")

#prompt the user to enter the other two values
if missing_value_choice == "1":
    a=float(input("Enter Acceleration (a): "))
    f=float(input("Enter Force (f): "))
    m=f/a
    print(f"Mass (m) = {m}")

elif missing_value_choice == "2":
    m=float(input("Enter Mass (m):" ))
    f=float(input("Enter Force (f):" ))
    a=f/m
    print(f"Acceleration (a) = {a}")

elif missing_value_choice == "3":
    m=float(input("Enter mass (m):"))
    a=float(input("Enter acceleration (a):"))
    f=m*a
    print (f"force (f)= {f}")

else:
    print ("invalid option selected for the missing value")
