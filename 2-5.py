from flask import Response, make_response

@app.route("/")
def response_test():
    constom_response = Response("Custom Response", 200, {
        "Program": "Flask Web"
    })

    return make_response(Custom)