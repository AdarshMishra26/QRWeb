from flask import Flask, render_template, request
import pyqrcode
import io
from base64 import b64encode

app = Flask(__name__)

# Function to generate QR code
def generate_qr_code(data):
    qr = pyqrcode.create(data)
    # Create a bytes IO stream to store the PNG image
    qr_stream = io.BytesIO()
    # Save the QR code to the bytes IO stream
    qr.png(qr_stream, scale=6)
    # Get the bytes of the PNG image from the stream
    qr_bytes = qr_stream.getvalue()
    # Encode the bytes as base64 string
    qr_base64 = b64encode(qr_bytes).decode('utf-8')
    return qr_base64

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['data']
        qr_code = generate_qr_code(data)
        return render_template('index.html', qr_code=qr_code, data=data)
    return render_template('index.html', qr_code=None, data=None)

if __name__ == '__main__':
    app.run(debug=True)
