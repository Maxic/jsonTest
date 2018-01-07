from flask import Flask, request, Response
from datetime import datetime
from pprint import pprint
import json

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
    data = request.form['payload']

    if (data is not None):
        js = json.dumps(data)
        print(js)
        print('What I want: ')
        print(js['actions']['value'])
    else:
        print("Received request, but no data")
    return Response(data, status=200)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)