from flask import Flask

app = Flask(__name__)

@app.route("/example/environ", methods=["GET", "POST"])
def example_environ():
    return request.endpoint

if __name__ == "__main__":
    app.run(host="0.0.0.0")
