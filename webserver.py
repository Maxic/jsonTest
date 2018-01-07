from flask import Flask, request, Response
import json
app = Flask(__name__)

@app.route("/slackTest", method=['POST'])
def receiveSlackMessages():
    data = request.get_json()
    if (data is not None):
        js = json.dumps(data)
        print("Json: " + js)
    else:
        print("Received request, but no data")
    return Response(data, status=200, mimetype='application/json')