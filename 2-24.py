from flask import Flask

app = Flask(__name__)

@app.route("/board/<article_id>")
@app.route("/board", defaults={"article_id":10})
def board(article_id):
    return "you are watcing {} no article".format(article_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0")