scores = [55,80,35,90,65]
print(f"Scores: {scores}")

scores.append(75)
print(f"Scores after append 75: {scores}")

scores[1] = 85
print(f"Scores after updating index 1: {scores}")

print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")

print(f"Average: {sum(scores)/len(scores)}")

for score in scores:
    if score >= 80:
        print(f"Scores 80 or above : {score}")