from flask import Flask, request

app = Flask(__name__)

@app.route("/board", methods=["GET", "POST"])
def board():
    return request.values.get("question")

if __name__ == "__main__":
    app.run(host="0.0.0.0")