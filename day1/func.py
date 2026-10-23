def cal_avg(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

scores = [40, 70, 50, 60, 30, 80]
average = cal_avg(scores)
print(f"Average: {average}")