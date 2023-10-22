import base64
from io import BytesIO
from PIL import Image

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/upload_image/<path:url>', methods=['POST'])
def upload_image(url):
    try:
        decoded_img = base64.b64decode(url)
        img = Image.open(BytesIO(decoded_img))

        img.save(url, 'HEIC')

        status = "Image have been successfully sent to the server."
    except Exception as e:
        status = "Error! = " + str(e)

    return status


if __name__ == '__main__':
    app.run()
