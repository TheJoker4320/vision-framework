from flask import Flask, Response
import cv2


class Streamer(object):
    def __init__(self):
        self.original_frame = None
        self.app = Flask("Streamer")
        self.app.add_url_rule("/feed", "feed", self._get_response)

    def run(self):
        self.app.run(host='0.0.0.0', port=80, debug=False, threaded=True)

    def update(self, original_frame):
        self.original_frame = original_frame

    @staticmethod
    def _get_img_bytes(img):
        _, img = cv2.imencode('.jpg', img)
        return img.tobytes()

    def _get_page(self):
        while True:
            frame = Streamer._get_img_bytes(self.original_frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    def _get_response(self):
        return Response(self._get_page(), mimetype='multipart/x-mixed-replace; boundary=frame')
