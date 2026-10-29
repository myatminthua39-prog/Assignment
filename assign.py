GRADE_CATEGORIES = ("Excellent", "Good", "Pass", "Fail")

def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def classify_grade(score):
    if 80 <= score <= 100:
        return GRADE_CATEGORIES[0]
    elif 60 <= score < 80:
        return GRADE_CATEGORIES[1]
    elif 40 <= score < 60:
        return GRADE_CATEGORIES[2]
    else:
        return GRADE_CATEGORIES[3]

def count_passed(students):
    passed_count = 0
    for student in students:
        if student["score"] >= 40:
            passed_count += 1
    return passed_count

def main():
    students = []
    
    print("--- Student Information Collection System ---")
    print("Please enter data for at least 5 students.\n")
    
    for i in range(1, 6):
        print(f"--- Student {i} ---")
        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))
        study_hours = float(input("Enter weekly study hours: "))
        
        while True:
            score = float(input("Enter Python score (0-100): "))
            if 0 <= score <= 100:
                break
            print("Invalid score! Scores outside the range 0-100 must be rejected or reported as invalid. Try again.")
        
        student_record = {
            "name": name,
            "age": age,
            "study_hours": study_hours,
            "score": score,
            "grade": classify_grade(score)
        }
        
        students.append(student_record)
        print()

    scores_list = [student["score"] for student in students]
    average_score = calculate_average(scores_list)
    total_passed = count_passed(students)

    print("\n" + "=" * 50)
    print("            ACADEMIC PERFORMANCE REPORT            ")
    print("=" * 50)
    for student in students:
        print(f"Name: {student['name']:<10} | Age: {student['age']} | Hours: {student['study_hours']:<4} | Score: {student['score']:<5} | Grade: {student['grade']}")
    print("-" * 50)
    print(f"Class Average Score: {average_score:.2f}")
    print(f"Total Passing Students: {total_passed} out of {len(students)}")
    print("=" * 50)

if __name__ == "__main__":
    main()