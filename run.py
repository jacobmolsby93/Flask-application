import os
from flask import Flask, render_template


app = Flask(__name__)


# @ == decorator
@app.route("/")
def index():
    # Flask expects the index.html file to be located in a folder called --> templates <--
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


# never have debug=True in a production ready application
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT","5000")),
        debug=True)
    