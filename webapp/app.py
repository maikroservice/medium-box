from flask import Flask, abort, render_template, request, send_file

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/videos")
def download_videos():
    blocklist = ["phar://", "zip://", "ftp://", "file://", "http://", "//", "data://", "expect://", "https://", "../", "./"]
    f_name = request.args.get('savefile')
    if f_name == None:
        return ""
    if any([f_name.startswith(item) for item in blocklist]):
        return "no video selected"
   
    else:
        try:
            return send_file(f_name, as_attachment=True)
        except FileNotFoundError:
            abort(404)


if __name__ ==  "__main__":
    app.run(debug=False)
