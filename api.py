from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/")
def index():
        if request.method=='GET':
             with open("json_file") as k:
                  data = json.load(k)
        return data


if __name__=="__main__":
    app.run(port=5000)