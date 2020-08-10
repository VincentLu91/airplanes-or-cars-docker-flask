from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from flask import Flask, render_template, request, redirect, url_for, abort, send_from_directory
import os
from PIL import Image

from werkzeug.utils import secure_filename

import imghdr
import shutil

port = int(os.environ.get("PORT", 5000))
app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png']
app.config['UPLOAD_PATH'] = 'uploads'

# load and prepare the image
def load_image(filename):
    img = Image.open(filename)
    img = img.resize((224,224),Image.ANTIALIAS)
    img = img_to_array(img)
    img = img.reshape(1, 224, 224, 3)
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    return img

# load an image and predict the class
def run_example(image):
    img = load_image(image)
    model = load_model('model.h5')
    result = model.predict(img)    
    if result[0] == [0.]:
        return 'The object identified in the photo is a plane'
    elif result[0] == [1.]:
        return 'The object identified in the photo is an automobile'
    else:
        return 'The object identified in the photo is neither a plane nor an automobile'

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    if not files:
        return render_template('index.html')
    else:
        image = files[0]
        result = run_example(os.path.join(app.config['UPLOAD_PATH'], image))
        return render_template('index.html', image=image, result=result)

@app.route('/', methods=['POST'])
def upload_files():
    error = None
    for root, dirs, files in os.walk('./uploads'):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                file_ext != validate_image(uploaded_file.stream):
            error = 'Invalid extension'
            return render_template('index.html', error=error)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)