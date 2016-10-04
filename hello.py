from flask import Flask
from flask import request
app = Flask(__name__)



@app.route("/")
def hello():
    return "Hello World!"
	
@app.route("/name/",methods=["GET"])
def name():
	yourName=request.args.get("name");
	return "Your name is: %s" %yourName

if __name__ == "__main__":
    app.run()