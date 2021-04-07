from flask import Flask, render_template, request, send_file, jsonify

####Functions for the user to interface with

#this will be empty in production
links = {"lights": {"var" : "one", "state": True}, "music": {"var" : "two", "state": False}, "play": {"var" : "three", "state": True}}

def bind(var, tag):
    #create a link between the variable and the web page
    pass




####Functions for us to use

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', len = len(links), links = links)

    

@app.route('/favicon.ico')
def favicon():
    return send_file("static/favicon.ico")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")