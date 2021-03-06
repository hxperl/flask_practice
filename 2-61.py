from flask import Flask, request

app = Flask(__name__)
app.config.update(MAX_CONTENT_LENGTH=1024*1024*10)

@app.route("/example/max_content_len", methods=["GET"])
def example_content_length():
    print(request.max_content_length)
    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)