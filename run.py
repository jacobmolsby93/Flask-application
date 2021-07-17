import os
import json
from flask import Flask, render_template


app = Flask(__name__)


# @ == decorator
@app.route("/")
def index():
    # Flask expects the index.html file to be located in a folder called templates
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    # open company.json and asign it to a new variable called json_data.
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


# never have debug=True in a production ready application
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT","5000")),
        debug=True)
    