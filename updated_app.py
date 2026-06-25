from flask import Flask, request, jsonify, render_template
import csv
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute(
        """
        create table if not exists student_data(
            rollNo integer primary key,
            name varchar(50) not null,
            year integer not null check(year >= 1 AND year <= 4)
        )
        """
    )
    cur.execute(
        """
        create table if not exists student_marks(
            mark_id integer primary key autoincrement,
            rollNo integer not null,
            subject_name text,
            mark_gained integer check(mark_gained >= 1 AND mark_gained <= 100),
            foreign key(rollNo) references student_data(rollNo)
        )
        """
    )
    conn.commit()
    conn.close()


@app.get("/")
def front_page():
    return render_template("navigateToSubjectPage.html")

@app.get("/temp")
def temp():
    return render_template("subject_form.html")

@app.get("/temp1")
def temp1():
    return render_template("delete-student.html")

@app.get("/temp2")
def temp2():
    return render_template("update-student.html")
@app.post("/students")
def students():
    conn = sqlite3.connect("students.db")
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    rno = request.form["roll_no"]
    name = request.form["name"]
    year = request.form["year"]
    try:
        cur.execute(
            "insert into student_data(rollNo, name, year) values(?, ?, ?)",
            (rno, name, year,)
        )
    except sqlite3.IntegrityError:
        conn.close()
        return "Roll number already exists"
    mark={}
    for temp in request.form:
        if temp.startswith("subject"):
            ind = temp.replace("subject", "")
            Sub = request.form[temp]
            Mark = request.form[f"marks{ind}"]

            mark[Sub] = Mark
    for subject, val in mark.items():
        cur.execute(
            "insert into student_marks(rollNo,subject_name, mark_gained) values(?, ?, ?)",
            (rno, subject, val,)
        )
    conn.commit()
    conn.close()
    return "student Added"


@app.post("/del-students")
def delete_students():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    id = request.form["del_rno"]
    cur.execute("delete from student_data where rollNo = ?",(id,))
    cur.execute("delete from student_marks where rollNo = ?",(id,))
    conn.commit()
    conn.close()
    return "student deleted"
    
@app.post("/subjects")
def subjects():
    n = int(request.form["subjects_num"])
    return render_template(
        "add-student.html",
        subjects_num = n
    )

@app.post("/update-students")
def update_students():
    sub_no = int(request.form["upd_sub_num"])

    return render_template(
        "main-update-student.html",
        upd_sub_num = sub_no
    )
@app.post("/upd")
def main_stud_update():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    roll = request.form["upd_rno"]
    try:
        for temp in request.form:
            if temp.startswith("sub_name"):
                ind = temp.replace("sub_name", "")
                Sub = request.form[temp]
                Mark = int(request.form[f"upd_marks{ind}"])
                cur.execute("update student_marks set mark_gained = ? where subject_name = ? and rollNo = ?",
                                (Mark, Sub, roll))
        conn.commit()
        conn.close()
        return "Student updated"
    
    except Exception as e:
        conn.close()
        return f"Error:{e}"
    
    
@app.get("/all")
def all_students():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    cur.execute(
        # "select * from student_data"
        "select * from student_data as sd join student_marks as sm on sd.rollNo = sm.rollNo"
    )
    rows = cur.fetchall()
    s = {}
    if not rows:
        return "No student found"
    else:
        for row in rows:
            rno = row[0]
            if rno not in s:
                s[rno]={
                    "Roll No":rno,
                    "Name":row[1],
                    "Year":row[2],
                    "Marks":[]
                }
            s[rno]["Marks"].append({
                    "subject":row[5],
                    "mark":row[6]
                })
    return s


if __name__ == "__main__":
    init_db()
    app.run(debug = True)