with open("students.txt", "w") as file:
    file.write("""Alice 85
Bob 90
Charlie 75
David 80
Emily 92
Frank 88
Grace 70
Henry 85
Ivy 78
Jack 95""")

students = {}
with open("students.txt", "r") as file:
    for line in file:
        name, score = line.split()
        score = int(score)
        if name in students:
            students[name].append(score)
        else:
            students[name] = [score]

average_scores = {name: sum(scores) / len(scores) for name, scores in students.items()}

all_scores = [score for scores in students.values() for score in scores]
highest_score = max(all_scores)
lowest_score = min(all_scores)
class_average = sum(all_scores) / len(all_scores)

score_counts = {}
for score in all_scores:
    if score in score_counts:
        score_counts[score] += 1
    else:
        score_counts[score] = 1

max_count = 0
mode = all_scores[0]

for score, count in score_counts.items():
    if count > max_count:
        max_count = count
        mode = score

with open("students_results.txt", "w") as file:
    for name, avg_score in average_scores.items():
        file.write(name + " " + str(avg_score) + " ")
    file.write("\nHighest Score: " + str(highest_score) + " ")
    file.write("Lowest Score: " + str(lowest_score) + " ")
    file.write("Class Average: " + str(class_average) + " ")