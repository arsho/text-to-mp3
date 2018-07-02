from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
from utils.converter import text_to_mp3
from utils.helpers import generate_card_body


AUDIO_FILE_FOLDER = 'generated_audio_files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = AUDIO_FILE_FOLDER


@app.route('/', methods=["GET", "POST"])
def index():
    try:
        data = None
        if request.method == "POST":
            input_text = request.form["input_text"]
            output_filename = secure_filename(request.form["output_filename"])
            audio_filename = text_to_mp3(input_text,
                                             app.config['UPLOAD_FOLDER'],
                                             output_filename)
            if audio_filename!=None:
                title = '<i class="fas fa-file-download"></i> Download '+audio_filename.split("/")[1]
                data = generate_card_body(request.url_root, audio_filename, title)
        if data!=None:
            return render_template("index.html", data=data)
        return render_template("index.html")
    except Exception as e:
        return str(e)

@app.route('/downloads/<path:filename>/')
def download_file(filename):
    try:
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
