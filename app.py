from flask import Flask, render_template, request, send_file, make_response
import io
from src.yt import download_audio_from_youtube
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form.get('url')
        audio_bytes, filename = download_audio_from_youtube(video_url)
        response = make_response(send_file(
            io.BytesIO(audio_bytes),
            as_attachment=True,
            download_name=filename,
            mimetype='audio/mpeg'
        ))
        response.set_cookie('downloadToken', 'true')
        return response
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('PORT', 5000))
