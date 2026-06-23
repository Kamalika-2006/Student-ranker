# from student_v2 import Student # imported student class from student.py module
# #main function to give inputs
# def main():
#     studs = Student.get_input()
#     for s in studs:
#         sub1, mark1 = s.high_score()
#         sub2, mark2 = s.low_score()
#         print(s)
#         print(f"Highest score in {sub1.upper()} with {mark1}")
#         print(f"lowest score in {sub2.upper()} with {mark2}")

# if __name__ == "__main__":
#     main()


#updated after file_manager.py
from student_v2 import Student
from file_manager import *

def main():
    students = Student.get_input()
    save_json(students)
    save_csv(students)
    print("\nLoaded from JSON")
    json_students = load_json()
    for s in json_students:
        print(s)
    print("\nLoaded from CSV")
    csv_students = load_csv()
    for s in csv_students:
        print(s)

if __name__ == "__main__":
    main()