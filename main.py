import json
import logging
import cv2

import collections
from threading import Thread
from streamer import Streamer

from camera import Camera
from pipeline.pipeline_factory import PipelineFactory
<<<<<<< HEAD
from networktables import NetworkTables
from remote_tuner import RemoteTuner
=======
import cv2
>>>>>>> 4bac9978eb6e56ecd036f7b69cf592b2a258a178


def main():
    logging.basicConfig(level=logging.INFO)

    with open("examples/example_circle.json", "r") as file_handler:
        properties = json.load(file_handler, object_pairs_hook=collections.OrderedDict)
    print properties
    my_pipeline = PipelineFactory.create_pipeline(properties)

    feed = Streamer()
    Thread(target=feed.run).start()
    camera_settings = properties['camera settings']
    camera = Camera(camera_settings['id'])
    camera.set_camera_settings(camera_settings)
    NetworkTables.initialize(server='10.43.20.69')
    r = RemoteTuner("examples/example_circle.json", my_pipeline)
    # frame = cv2.imread('ball.jpg')
    feed = Streamer()
    Thread(target=feed.run).start()
    # frame = cv2.imread('diagonal_test.jpg')
    
    while True:
        frame = camera.get_frame()
        processed_frame = my_pipeline.process_image(frame)
        my_pipeline = r.get_pipeline()
        feed.update(processed_frame)


if __name__ == "__main__":
    main()
