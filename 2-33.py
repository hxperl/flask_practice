from flask import Flask, request

app = Flask(__name__)

@app.route("/board")
def board_list():
    return "The variable value of 'question' from query string is {}".format(request.args.get('question'))

if __name__=="__main__":
    app.run(host="0.0.0.0")