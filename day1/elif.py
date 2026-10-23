marks = float(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks. Please enter a value between 0 and 100.") 
elif marks >= 80:
    print("Excellent!")
elif marks >= 60:
    print("Good job!")
elif marks >= 40:
    print("Passed")
else:
    print("You have failed the exam.")