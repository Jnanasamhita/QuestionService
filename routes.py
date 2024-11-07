from flask import Flask, request, render_template
from backend.pandasimporter import csvToListDict
import json

app = Flask('__main__')


@app.route("/", methods=['GET'])
def getData():
    return json.load({
        "name": "Pranav",
        "request_type": "GET"
    })


@app.route("/upload/", methods=["GET", "POST"])
def uploadCSV():
    if request.method == 'POST':
        file = request.files['questionsCSV']
        content: str = file.read().decode('UTF-8')
        print(content)
        print(csvToListDict(content))
    return render_template('upload.html')
