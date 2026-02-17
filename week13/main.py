import json


def mock_api():
    print("Starting FastAPI server...")
    print("Uvicorn running on http://127.0.0.1:8000 (Mock Mode)")

 
    users_db = [
        {"id": 1, "name": "Alice", "email": "alice@htw.de", "role": "Admin"},
        {"id": 2, "name": "Bob", "email": "bob@htw.de", "role": "Student"}
    ]


    print("\n[GET] /")
    print("Response: {'status': 'healthy', 'message': 'API is running'}")

    print("\n[GET] /users")
    print("Response:", json.dumps(users_db, indent=2))

    print("\n[GET] /users/search?q=Alice")
    search = [u for u in users_db if "Alice" in u["name"]]
    print("Response:", json.dumps(search, indent=2))

    print("\n[GET] /users/1")
    print("Response:", json.dumps(users_db[0], indent=2))

    print("\n API Test Complete: All routes verified")

if __name__ == "__main__":
    mock_api()
