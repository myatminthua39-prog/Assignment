scores = [40, 70, 50, 60, 30, 80]

def cal_total(scores):
    total = 0
    for score in scores:
        total += score
    return total
print(f"Total: {cal_total(scores)}")

def cal_avg(scores):
    if len(scores) == 0:
        return 0
    return cal_total(scores) / len(scores)
print(f"Average: {cal_avg(scores)}")

def grade(scores):
    for score in scores:
        if score < 0 or score > 100:
            print("Invalid")
        elif score >= 80:
            print(f"Score: {score}", " -Excellent")
        elif score >= 60:
            print(f"Score: {score}", " -Good job!")
        elif score >= 40:
            print(f"Score: {score}", " -Passed")
        else:
            print(f"Score: {score}", " -You have failed the exam.")

def no_passed(scores):
    no_passed = 0
    for score in scores:
        if score >= 40:
            no_passed += 1
    print(f"Number of students passed: {no_passed}")

cal_total(scores)
cal_avg(scores)
grade(scores)
no_passed(scores)