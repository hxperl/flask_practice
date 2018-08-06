from flask import Flask

app = Flask(__name__)

@app.route("/")
def http_prepost_response():
    return "/"

@app.before_first_request
def before_first_request():
    print("Response to only first http request after app start")

@app.before_request
def before_request():
    print("Execute before handle http request")

@app.after_request
def after_request():
    print("Execute After handle http request")

@app.teardown_request
def teardown_request(exception):
    print("called after every http request responded to browser")

@app.teardown_appcontext
def teardown_appcontext(exception):
    print("Execute when application of http request exit")

if __name__ == "__main__":
    app.run(host="0.0.0.0")