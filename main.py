@app.post("/users")
def add_user(user: dict):
    users = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            users = json.load(f)

    # Check if user already exists
    for existing_user in users:
        if existing_user["email"] == user["email"]:
            return {"message": "User with this email already exists"}

    # If the user doesn't exist, add it
    users.append(user)
    with open(DATA_FILE, "w") as f:
        json.dump(users, f)
    return {"message": "User added"}
