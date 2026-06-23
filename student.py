#student class to add students, get the highest and lowest score obtained and compute the average 
#this class is inherited in demo.py

class student:
    def __init__(self, name, year, marks):
        self.name = name
        self.year = year
        self.marks = marks  # "Marks" ,a dictionary that stores subject->Key and mark -> values

    def compute_average(self):
        sum = 0
        i = 0
        for sub,score in self.marks.items():
            i += 1
            sum += score
        return sum/i
    
    def high_score(self): 
        first = 0
        for sub, mark in self.marks.items():
            if mark > first:
                first = mark
                res = sub
        return res, first
    
    def low_score(self):
        last = 100
        for sub, mark in self.marks.items():
            if mark < last:
                last = mark
                res = sub
        return res, last
    
    # __str__ helps in printing the object with a specified representation
    def __str__(self):
        return (
            f"Student: {self.name}\n"
            f"Year: {self.year}\n"
            f"Average: {self.compute_average():.2f}"
        )
    
    @classmethod #can be accessed without object like "student.get_input()"
    def get_input(cls):
        students_list= [] # to store students 
        subs= [] # subjects
        
        number_of_stud = int(input("Enter the number of students to add:"))
        n = int(input("Enter the number of subjects: "))
        year = int(input("Enter the year:"))
        
        for i in range(n):
            temp = input(f"Enter the subject {i+1} name: ")
            subs.append(temp)

        for i in range(number_of_stud):
            marks = {} # dict
            name = input("Enter the name of the student:")
            for s in subs:
                while True:
                    mark = float(input(f"Enter the marks obtained for {s}:"))
                    if mark <0 or mark >100:
                        print("Invalid mark entered. Enter again!")
                    else:
                        marks[s] = mark
                        break
            obj = student(name, year, marks)
            students_list.append(obj)

        return students_list