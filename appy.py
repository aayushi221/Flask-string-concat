from flask import Flask

app = Flask(__name__)
users = [{"name": "Me"}, {"name": "main"}, {"name": "Goblin"}, {"name": "K"}]


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/user", methods=["GET"])
def hello():
  users.append({
      "name" : "Aayushi"
  })
  return f"user added at {len(users)-1}th position "


@app.route("/user/<int:user_id>")
def show_user_profile(user_id):
    try:
        return f"user id {users[user_id]} "
    except:
        return "user not found"


if __name__ == "__main__":
    app.run(debug=True)