from flask import Flask,request
import requests
app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World'

@app.route("/calculator/add", methods=['POST'])
def add():
    temp = requests.json
    a = int(temp["first"])
    b = int(temp["second"])
    return { "result" : a + b}


@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    temp = requests.json
    a = int(temp["first"])
    b = int(temp["second"])
    return { "result" : a - b}

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
