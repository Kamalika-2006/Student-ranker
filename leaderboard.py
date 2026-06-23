from file_manager import load_csv
from student_v2 import Student
def student_leaderboard():
    students = load_csv()
    if not students:
        print("No students found!")
        return
    
    ranked_students = sorted(
        students,
        key = lambda x:x.compute_average(),
        reverse = True
    )
    print("\nALLL Ranked students\n")

    print(
        f"{'Rank':<6}"
        f"{'Name':<15}"
        f"{'Year':<8}"
        f"{'Average':<10}"
    )
    for r, studs in enumerate(ranked_students, start = 1):
        print(
            f"{r:<6}"
            f"{studs.name:<15}"
            f"{studs.year:<8}"
            f"{studs.compute_average():<10.2f}"
        )
    print("\nTop 3 Students\n")
    # to print the top 3 students based on average
    for i,s in enumerate(ranked_students[:3], start = 1):
        print(
            f"{i:<6}"
            f"{s.name:<15}"
            f"{s.compute_average():<10.2f}"
        )

    print("\nBOTTOM 3 STUDENTS")
    bottom_studs=ranked_students[-3:]
    for i,s1 in enumerate(bottom_studs):
        print(
            f"{s1.name:<15}"
            f"{s1.compute_average():<10.2f}"
        )

    class_avg= sum(sd.compute_average() for sd in students)/len(students)

    print(f"The Class Average:{class_avg}")

if __name__ == "__main__":
    student_leaderboard()