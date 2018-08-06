from flask import Flask

app = Flask(__name__)

@app.route("/board", redirect_to="/new_board")
def board():
    return "/board URL called but would not be executed"

@app.route("/new_board")
def new_board():
    return "/new_board called"

if __name__ == "__main__":
    app.run(host="0.0.0.0")