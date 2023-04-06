from flask import Flask, render_template, Response, request
import cv2
import numpy as np
import pyautogui

app = Flask(__name__)

# Set up a global variable for storing the most recent screenshot
global_frame = None
size = pyautogui.size()

@app.route('/')
def index():
    return render_template('index.html')


def gen():
    global global_frame
    while True:
        if global_frame is not None:
            # Convert the global frame to a JPEG image
            ret, jpeg = cv2.imencode('.jpg', global_frame)
            # Return the JPEG image as a byte stream
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/upload', methods=['POST'])
def upload():
    global global_frame
    # Receive the data from the client
    data = request.data
    # Convert the data to a numpy array
    frame = np.frombuffer(data, dtype=np.uint8)
    # Reshape the numpy array to the screen size
    screen_size = (size.height, size.width, 3)
    frame = frame.reshape(screen_size)
    # Store the frame in the global variable
    global_frame = frame
    # Return a success response
    return 'OK'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
