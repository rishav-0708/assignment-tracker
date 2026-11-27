from flask import Flask, request, redirect

app = Flask(__name__)

assignments = []

@app.route("/")
def home():
    page = """
    <h1>Student Assignment Tracker</h1>
    <form action="/add" method="post">
        <input name="title" placeholder="Assignment" required>
        <input type="date" name="deadline" required>
        <button>Add Assignment</button>
    </form>
    """

    for a in assignments:
        page += f"<p>{a['title']} - {a['deadline']} - {a['status']}</p>"

    return page

@app.route("/add", methods=["POST"])
def add():
    assignments.append({
        "title": request.form["title"],
        "deadline": request.form["deadline"],
        "status": "Pending"
    })
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
