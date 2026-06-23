from flask import Flask, request, render_template
import csv

app = Flask(__name__)

@app.get("/")
def front_page():
    return render_template("navigateToSubjectPage.html")

@app.get("/temp")
def temp():
    return render_template("subject_form.html")

@app.post("/students")
def students():
    rno = request.form["roll_no"]
    name = request.form["name"]
    year = request.form["year"]

    mark={}
    for temp in request.form:
        if temp.startswith("subject"):
            ind = temp.replace("subject", "")
            Sub = request.form[temp]
            Mark = request.form[f"marks{ind}"]

            mark[Sub] = Mark
    rows = [rno, name, year]
    for i, m in mark.items():
        rows.append(m)
    
    with open("./csvFiles/students_v2.csv", "a", newline="") as f:
        wt = csv.writer(f)
        wt.writerow(rows)
    return "student Added"



@app.post("/subjects")
def subjects():
    n = int(request.form["subjects_num"])
    return render_template(
        "add-student.html",
        subjects_num = n
    )

if __name__ == "__main__":
    app.run(debug = True)