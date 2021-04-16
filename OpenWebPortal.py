from flask import Flask, render_template, request, send_file, jsonify
import threading

####Functions for the user to interface with

#this will be empty in production
links = {}

class OWP():
    def __init__(self, name, value):
        self.value = value
        self.name = name
        links[name]={"state": value, "object": self}

    def value(self):
        return self.value

    def update(self, value):
        self.value = value
        links[self.name]["state"] = value

def start():
    threading.Thread(target=app.run).start()
    links = {}


####Functions for us to use

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', len = len(links), links = links)


@app.route('/update/<Variable>/<newValue>')
def update(Variable, newValue):
    links[Variable]["object"].update(newValue)

    return (jsonify(success=True))

    

@app.route('/favicon.ico')
def favicon():
    return send_file("static/favicon.ico")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")