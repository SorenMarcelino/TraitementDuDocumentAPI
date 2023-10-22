import os
import base64
from io import BytesIO
from PIL import Image

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/upload_image', methods=['POST'])
def upload_image():
    try:
        # Get the base64 image data from the request
        data = request.get_json()
        base64_image = data.get('image', '')

        # Decode the base64 image data
        image_data = base64.b64decode(base64_image)

        # Save the image to a file
        with open("uploaded_image.png", "wb") as image_file:
            image_file.write(image_data)

        # Process or use the image data as needed
        # TO DO

        # Respond with a success message
        response = {
            'message': 'Image uploaded successfully'
        }
        return jsonify(response), 200

    except Exception as e:
        # Handle any errors that might occur
        error_message = {'error': str(e)}
        return jsonify(error_message), 400


if __name__ == '__main__':
    app.run()
