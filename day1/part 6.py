
scores = [40,70,50,60,30,80]

total = 0

for score in scores:
    total += score

average = total / len(scores)
print(f"Total: {total}")            
print(f"Average: {average}")

number_of_failing = 0
number_of_passing = 0

for score in scores:                    #for loop ပြီးရင် condition စစ် output ထွက်တာကို အပြင်မှာ ထုတ်
    if score < 40:
        number_of_failing += 1       
    elif score >= 40:
        number_of_passing += 1
        

print (f"number of failing students: {number_of_failing}")
print (f"number of passing students: {number_of_passing}")