from flask import Flask, request, redirect
from markupsafe import escape

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
    <hr>
    """

    for i, a in enumerate(assignments):
        page += f"""
        <div>
            {escape(a['title'])} -
            {escape(a['deadline'])} -
            {a['status']}

            <form action="/complete/{i}" method="post">
                <button>Complete</button>
            </form>
        </div>
        <hr>
        """

    return page


@app.route("/add", methods=["POST"])
def add():
    assignments.append({
        "title": request.form["title"],
        "deadline": request.form["deadline"],
        "status": "Pending"
    })

    return redirect("/")


@app.route("/complete/<int:id>", methods=["POST"])
def complete(id):
    if 0 <= id < len(assignments):
        assignments[id]["status"] = "Completed"

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
