from flask import Flask, render_template
from functions import convert_to_qr

app = Flask("__main__")


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def contact():
    return render_template("about.html")

@app.route("/api/<data>")
def qr_generator(data):
    imgData = convert_to_qr(data)
    return f"data:image/png;base64,{imgData}"

if __name__ == "__main__":
    app.run(debug=True)