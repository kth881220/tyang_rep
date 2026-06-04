students = [
    {"name": "김철수", "math": 85, "english": 90, "science": 78},
    {"name": "이영희", "math": 92, "english": 88, "science": 95},
    {"name": "박민수", "math": 76, "english": 65, "science": 80},
    {"name": "김태황", "math": 91, "english": 98, "science": 90},
    {"name": "박경원", "math": 70, "english": 62, "science": 81},
]

for student in students:
    avg = round((student["math"] + student["english"] + student["science"]) / 3, 1)
    if avg >= 90:
        grade = "A등급"
    elif avg >= 80:
        grade = "B등급"
    elif avg >= 70:
        grade = "C등급"
    else:
        grade = "F등급"
    print(student["name"], "| 평균", avg, "|", grade)


top_name = ""
top_avg = 0
for student in students:
    avg = round((student["math"] + student["english"] + student["science"]) / 3, 1)
    if avg > top_avg:
        top_name = student["name"]
        top_avg = avg

print("1등:", top_name, "(" + str(top_avg) + "점)")

with open("result.txt", "a") as f:
    f.write("1등: " + top_name + " (" + str(top_avg) + "점)\n")