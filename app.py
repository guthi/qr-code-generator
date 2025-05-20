import os
import qrcode
from flask import Flask, render_template, request, send_file
from uuid import uuid4

app = Flask(__name__)
QR_FOLDER = "static/qr_codes"
os.makedirs(QR_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_path = None

    if request.method == "POST":
        data = request.form.get("text")
        if data:
            filename = f"{uuid4().hex}.png"
            filepath = os.path.join(QR_FOLDER, filename)
            qr_img = qrcode.make(data)
            qr_img.save(filepath)
            qr_path = filepath

    return render_template("index.html", qr_path=qr_path)

@app.route("/download/<filename>")
def download_qr(filename):
    path = os.path.join(QR_FOLDER, filename)
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
