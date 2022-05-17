friends_ages = {
    "Rolf": 24,
    "Adam": 30,
    "Anne": 27
}

friends_ages["Anne"] = 36
print(friends_ages)

friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 35},
]

print(friends[1]["name"])

student_attendance = {"Rolf": 98, "Bob": 75, "Anne": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("Bob is not a student in this class")

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))