from flask import Flask


app=Flask(__name__)


@app.route("/",methods=["GET"])
def home():
    return "This is the home page"



@app.route("/score",methods=["GET"])
def score():
    return "score page"


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)