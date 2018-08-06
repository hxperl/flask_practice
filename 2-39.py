from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

def dateKoreanType(date_format):
    def translate(date_str):
        return datetime.strptime(date_str, date_format)
    return translate

@app.route("/board", methods=["GET", "POST"])
def board():
    print(request.values.get("date", "2015-02-09", type=dateKoreanType("%Y-%m-%d")))
    return "check ur console"