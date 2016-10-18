import flask as fl
import itertools as it
app = fl.Flask(__name__)



@app.route("/")
def hello():
    return app.send_static_file("index.html")
	#redirects the user to the index
	#"static" means it doesnt change and is in the static folder
	
@app.route("/name",methods=["Post"])
def name():
	if request.method == "POST":
		yourName=request.form["name"];
		return "Your name is: %s" %yourName
	else:
		return "Errorrrr"

@app.route("/perms/")
def perms():
	perms = [''.join(p) for p in it.permutations(fl.request.args.get("userinput"))]
	return '\n'.join(perms)

if __name__ == "__main__":
    app.run()