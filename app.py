from flask import Flask, request, Response
from datetime import datetime
import json
from pprint import pprint
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400">
    """.format(time=the_time)

@app.route("/slackTest", methods=['POST'])
def receiveSlackMessages():
    pprint(vars(request))
    pprint(dir(request))
    data = request.data['payload']
    if (data is not None):
        js = json.dumps(data)
        print("Json: " + js)
        print("Data: " + data)
    else:
        print("Received request, but no data")
    return Response(data, status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)