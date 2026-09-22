while True:
    age = int(input("Enter your age; "))
    if age < 13:
        print("Sorry, you are not allowed to pass")
    elif age >= 13 and age < 18:
        print("Call your legal gueardian")
    elif age >= 18: 
        print("Welcome")