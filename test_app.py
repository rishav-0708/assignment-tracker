from app import app, assignments

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_add():
    assignments.clear()
    client = app.test_client()

    client.post("/add", data={
        "title": "ASE",
        "deadline": "2026-11-30"
    })

    assert len(assignments) == 1

def test_complete():
    assignments.clear()
    client = app.test_client()

    client.post("/add", data={
        "title": "ASE",
        "deadline": "2026-11-30"
    })

    client.post("/complete/0")

    assert assignments[0]["status"] == "Completed"
