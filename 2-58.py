from flask import Flask, request

app = Flask(__name__)

@app.route("/example/rule", methods=["GET", "POST"])
def example_rule():
    return request.url_rule

if __name__ == "__main__":
    app.run(host="0.0.0.0")