from flask import Flask, Response

app = Flask(__name__)

@app.route("/cookie_set")
def cookie_set():
    custom_resp = Response("Cookie setting")
    custom_resp.set_cookie("ID", "JPUB Flask Programming")

    return custom_resp
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)