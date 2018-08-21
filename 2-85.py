from flask import Flask
import logging

app = Flask(__name__)
app.config.update(DEBUG=True)
app.debug_log_format = "%(levelname)s in %(module)s [%(lineno)d]: %(message)s"

@app.route("/log")
def logger():
    app.logger.debug("printed DEBUG message")
    return "flask instane "

app.run(host="0.0.0.0")