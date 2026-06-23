import json, csv
from student_v2 import Student

def save_json(students, filename="students.json"):
    data = []
    for s in students:
        stud_dict = {
            "name": s.name,
            "year": s.year,
            "marks": s.marks
        }
        data.append(stud_dict)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Student data saved to {filename}")


def load_json(filename="students.json"):
    students = []
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            for record in data:
                obj = Student(
                    record["name"],
                    record["year"],
                    record["marks"]
                )
                students.append(obj)
    except FileNotFoundError:
        print(f"{filename} not found.")
    return students


def save_csv(students, filename="students.csv"):
    if not students:
        print("No students to save.")
        return
    subjects = list(students[0].marks.keys())
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        header = ["name", "year"] + subjects
        writer.writerow(header)
        for s in students:
            row = [s.name, s.year]
            for sub in subjects:
                row.append(s.marks[sub])
            writer.writerow(row)
    print(f"Student data saved to {filename}")


def load_csv(filename="students.csv"):
    import os

    students = []
    # Resolve relative path against this file's directory
    base_dir = os.path.dirname(__file__)
    filepath = filename if os.path.isabs(filename) else os.path.join(base_dir, filename)

    try:
        with open(filepath, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row["name"]
                year = int(row["year"])
                marks = {}
                for key, value in row.items():
                    if key not in ["name", "year"]:
                        marks[key] = float(value)
                obj = Student(name, year, marks)
                students.append(obj)
    except FileNotFoundError:
        print(f"{filepath} not found.")
    return students
