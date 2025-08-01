from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

@app.route("/", methods=["GET", "POST"])
def index():
    qr_code = None
    if request.method == "POST":
        data = request.form["data"]
        img = qrcode.make(data)
        path = os.path.join(app.config['UPLOAD_FOLDER'], "qr.png")
        img.save(path)
        qr_code = "qr.png"
    return render_template("index.html", qr_code=qr_code)

if __name__ == "__main__":
    app.run(debug=True)
