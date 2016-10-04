from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
	
@app.route("/name/<yourName>")
def name(yourName):
	return "Your name is: %s" %yourName

if __name__ == "__main__":
    app.run()