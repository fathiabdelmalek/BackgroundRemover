import os
from io import BytesIO

from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file, Response
from rembg import remove
from PIL import Image


load_dotenv()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file() -> str | Response:
    if request.method == 'POST':
        if 'file' not in request.files:
            return Response('No file uploaded', 400)
        file = request.files['file']
        if file.filename == '':
            return Response('No file selected', 400)
        if file:
            input_image = Image.open(file.stream)
            output_image = remove(input_image, post_process_mask=True)
            img_io = BytesIO()
            output_image.save(img_io, 'PNG')
            img_io.seek(0)
            return send_file(img_io, mimetype='image/png', as_attachment=True, download_name=f"{file.filename}")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.getenv("DEBUG"))
