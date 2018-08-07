from flask import Flask, request, session

app = Flask(__name__)

app.secret_key = 'asdf'

@app.route("/session_set")
def session_set():
    session['ID'] = 'JPUB Flask Session Setting'
    return "session created"

@app.route("/session_out")
def session_out():
    del session['ID']
    return "session removed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)