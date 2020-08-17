from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/settings', methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        colour = request.form["bgcolour"]
        text = request.form["name"]
        print(colour)
        print(text)
    
    return render_template('settings.html')

@app.route('/settings.json')
def settingsjson():
    return send_file("settings.json")

@app.route('/favicon.ico')
def favicon():
    return send_file("favicon.ico")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")