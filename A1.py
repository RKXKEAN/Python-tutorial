scores_dict = {}
for person in range(1, 6):
    scores = input().split()
    total = 0
    for score in scores:
        total += int(score)
    scores_dict[person] = total

print(scores_dict)

maximum_score = max(scores_dict.values())
for key, value in scores_dict.items():
    if value == maximum_score:
        print(key, value)
