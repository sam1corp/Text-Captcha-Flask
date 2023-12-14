from PyCaptcha import generate
from flask import Flask, render_template

app = Flask(__name__)
key = generate(6)  # First Captcha Key Generation


@app.route("/")
def home():
    return render_template("index.html", captcha=key)


@app.route("/refreshCaptcha")
def refresh():
    key = generate(6)  # New Captcha Key Generation
    return render_template("index.html", captcha=key)


if __name__ == "__main__":
    app.run(debug=False)
