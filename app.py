import os
from flask import Flask, render_template, request, redirect, send_file, url_for
from s3 import download_file, upload_file, list_files

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "itglue-daniel"




@app.route("/")
def storage():
    contents = list_files("itglue-daniel")

    return render_template('s3.html', contents=contents)


@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(f.filename)
        upload_file(f.filename, BUCKET)
        # TODO Change to url for storage on ec2/container
        return redirect(url_for('storage'))


@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = download_file(filename, BUCKET)

        return send_file(output, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
