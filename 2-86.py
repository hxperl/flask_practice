from flask import Flask
import logging

app = Flask(__name__)
app.config.update(DEBUG=True)

file_log_format = logging.Formatter('%(levelname)-8s %(message)s')

file_logger = logging.FileHandler("flask_instance.log")

file_logger.setFormatter(file_logger)

app.logger.addHandler(file_logger)

@app.route("/log")
def logger():
    app.logger.debug("print DEBUG message")
    return "check console"

app.run(host="0.0.0.0")