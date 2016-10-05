from flask import Flask
from flask import request,url_for,redirect
app = Flask(__name__)



@app.route("/")
def hello():
    return redirect (url_for('static', filename='index.html'))
	#redirects the user to the index
	#"static" means it doesnt change and is in the static folder
	
@app.route("/name",methods=["Post"])
def name():
	if request.method == "POST":
		yourName=request.form["name"];
		return "Your name is: %s" %yourName
	else:
		return "Errorrrr"

if __name__ == "__main__":
    app.run()