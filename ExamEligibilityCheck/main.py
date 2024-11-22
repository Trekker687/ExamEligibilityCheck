medical =  input("Do you have a medical condition? True/False")
attendance = int(input("Enter the percentage attendance"))

if medical == "True" :
    print("You are eligible to write the exams")
else :
    if attendance >= 75 and attendance <= 100 :
        print("You are eligible to write the exams")
    elif attendance < 75 :
        print("You are not eligible to write the exams")
    else:
        print("Invalid")

