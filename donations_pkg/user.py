def login(database, username, password):
    if username in database and password == database[username]:
        print("\nWelcome back", username + "!")
        return username
    elif username in database and password != database[username]:
        print("\nIncorrect password for", username + ".")
        return ""
    else:
        print("\nUser not found. Please register.")
        return ""


def register(database, username):
    if username in database:
        print("\nUsername already registered.")
        return ""
    else:
        print("\nUsername", username, "registered!")
        return username
