from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        return render_template("result.html", name=name)
    return render_template("index.html")

app.run(debug=True)
