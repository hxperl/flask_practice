from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

class dateKoreanType:
    def __init__(self, format):
        self.format = format

    def __call__(self, *args, **kwargs):
        return datetime.strptime(args[0], self.format)

@app.route("/board", methods=["GET", "POST"])
def board():
    print(request.values.getlist("dates", type=dateKoreanType("%Y-%m-%d")))
    return "check ur console"

if __name__ == "__main__":
    app.run(host="0.0.0.0")