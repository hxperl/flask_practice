from flask import Flask
import logging

app = Flask(__name__)
app.config.update(DEBUG=True)

@app.route("/log")
def logger():
    app.logger.debug("print DEBUG message")
    return "check console"

app.run(host="0.0.0.0")