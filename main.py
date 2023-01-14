from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
download_desktop = "https://docs.google.com/document/d/1-4o2M_YJY1axbgIV8oZ2PMzQtMCpMCpTFGPmyngkep0/edit?usp=sharing"
download_apk = "https://docs.google.com/document/d/1-4o2M_YJY1axbgIV8oZ2PMzQtMCpMCpTFGPmyngkep0/edit?usp=sharing"

@app.route("/", methods=["POST","GET"])
def homepage():
    return render_template("homepage.html")

@app.route("/download", methods=["POST","GET"])
def features():
    return render_template("download.html")

@app.route("/login", methods=["POST","GET"])
def login():
    return render_template("login.html")

@app.route("/signup", methods=["POST","GET"])
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)
