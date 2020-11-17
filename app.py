from flask import Flask, render_template, request, send_file, jsonify
import savesettings as s

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/settings', methods=["GET", "POST"])
def settings():
    return render_template('settings.html')

@app.route('/savesettings', methods=["POST"])
def savesettings():
    if request.method == "POST":
        data = request.form["data"].split("&")
        for element in range(len(data)):
            data[element] = data[element].split("=")
            data[element] = data[element][1].replace("%23", "#")
        print(data)
        for item in range(len(data)):
            s.save(str(item+1), data[item])
    return ('', 204)

@app.route('/settings.json')
def settingsjson():
    return send_file("settings.json")
    

@app.route('/favicon.ico')
def favicon():
    return send_file("static/favicon.ico")#

@app.route('/style.css')
def stylesheet():
    return send_file("/static/style.css")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")