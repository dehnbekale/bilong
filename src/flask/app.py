from flask import Flask, render_template, session, redirect, url_for, request


app = Flask(__name__)

@app.route("/")
def home():
    """
    home
    """
    name = "Bilong"
    return render_template("home.html", param=name)


if __name__ == "__main__":
    app.run(debug=True)