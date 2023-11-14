from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<a href='https://www.naver.com'>네이버</a>"

@app.route("/home")
def goHome():
    return ("")

app.run(host='0.0.0.0', port=int(80))