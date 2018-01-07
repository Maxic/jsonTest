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
    print("PRINTING REQUEST FORM")
    pprint(request.form)

    print("FORM.KEYS[0]")
    pprint(list(request.form.keys())[0])

    data = list(request.form.keys())[0]

    if (data is not None):
        print("Print data[0]: ")
        pprint(data[0])
        #js = json.dumps(data['payload'])
        #print(js)
    else:
        print("Received request, but no data")
    return Response(data, status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)