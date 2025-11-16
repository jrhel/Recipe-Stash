from dao import db_connection_handler

def create_user(username: str, password_hash: str):
    print("UserDAO: Create account for:", username)
    params = [username, password_hash]
    id = db_connection_handler.execute("INSERT INTO User (username, password_hash) VALUES (?, ?)", params)
#    return get_user("id", id)[1]

def get_user(username):
    print("GETTING USER", username)
    params = [username]
    result = db_connection_handler.query("SELECT * FROM User WHERE username = ?", params)[0]
    user = {}
    user["id"] = result[1]
    user["username"] = result[1]
    user["password_hash"] = result[2]
    print("USER =", user)
    return user