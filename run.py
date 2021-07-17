import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


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


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data: 
            if obj["url"] == member_name:
                member = obj
    # first member == member.html, the second member is the empty object declared in the beggining of this function
    return render_template("member.html", member=member)

# to comply with the pep8 compliance of line not longer than 79char, enter just after opening braces.
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


# never have debug=True in a production ready application
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
    