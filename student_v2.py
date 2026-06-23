#student class to add students, get the highest and lowest score obtained and compute the average 
#this class is inherited in demo.py

import logging

logging.basicConfig(
    filename="student_logs.log",
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class InvalidScore(Exception): #Here the class InvalidScore inherits the parent class Exception
    def __init__(self, sub, mark):
        self.sub = sub
        self.mark = mark

        if isinstance(mark, str):
            super().__init__("Invalid score. Mark should be numeric!")
        else:
            super().__init__(f"Invalid score for {sub}. Marks must be between 0 and 100.")


class InvalidName(Exception): #Here the class InvalidName inherits the parent class Exception
    def __init__(self, name):
        self.name = name

        if isinstance(name, (int, float)):
            super().__init__("Name should not be a number!")
        else:
            super().__init__("Invalid name. Name should not be empty or blank.")


class Student:
    def __init__(self, name, year, marks):
        if not name or not name.strip():
            raise InvalidName(name)

        for sub, mark in marks.items():
            if not isinstance(mark, (int, float)) or not (0 <= mark <= 100):
                raise InvalidScore(sub, mark)

        self.name = name
        self.year = year
        self.marks = marks # "Marks", a dictionary that has subject as a key and it marks as a value

    def compute_average(self):
        if not self.marks:
            return 0.0

        total = 0

        for score in self.marks.values():
            total += score

        return total / len(self.marks)

    def high_score(self):
        if not self.marks:
            return None, 0.0

        sub = max(self.marks, key=self.marks.get)
        return sub, self.marks[sub]

    def low_score(self):
        if not self.marks:
            return None, 0.0

        sub = min(self.marks, key=self.marks.get)
        return sub, self.marks[sub]

    def __str__(self):
        return (
            f"Student: {self.name}\n"
            f"Year: {self.year}\n"
            f"Average: {self.compute_average():.2f}"
        )

    @classmethod
    def get_input(cls):
        students_list = [] # to store an objects of students

        try:
            subs = []

            number_of_stud = int(input("Enter the number of students to add: "))
            n = int(input("Enter the number of subjects: "))
            year = int(input("Enter the year: "))

            if number_of_stud <= 0:
                raise ValueError("Number of students must be positive.")

            if n <= 0:
                raise ValueError("Number of subjects must be positive.")

            for i in range(n):
                temp = input(f"Enter the subject {i+1} name: ")

                if not temp or not temp.strip():
                    logging.error("Empty subject name entered")
                    raise ValueError("Subject name cannot be empty.")

                subs.append(temp)

            for i in range(number_of_stud):
                marks = {}

                name = input("Enter the name of the student: ")

                if not name or not name.strip() or name.isdigit():
                    logging.error("Invalid student name entered")
                    raise InvalidName(name)

                for s in subs:
                    try:
                        mark = float(input(f"Enter the marks obtained for {s}: "))
                    except ValueError:
                        logging.error(f"ScoreError detected: non-numeric mark entered for {s}")
                        raise InvalidScore(s, "invalid")

                    if not (0 <= mark <= 100):
                        logging.error(f"ScoreError detected: mark {mark} out of range")
                        raise InvalidScore(s, mark)

                    marks[s] = mark

                obj = cls(name, year, marks)
                students_list.append(obj)

        except (InvalidScore, InvalidName, ValueError) as e:
            print(f"Error: {e}")
            return []

        else:
            print("Students added successfully!")
            return students_list