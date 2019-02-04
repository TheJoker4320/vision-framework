import json
import logging
import cv2

import collections
from threading import Thread
from streamer import Streamer

from camera import Camera
from pipeline.pipeline_factory import PipelineFactory
from networktables import NetworkTables
from remote_tuner import RemoteTuner


def main():
    logging.basicConfig(level=logging.INFO)

    with open("examples/example_circle.json", "r") as file_handler:
        properties = json.load(file_handler, object_pairs_hook=collections.OrderedDict)
    print properties
    my_pipeline = PipelineFactory.create_pipeline(properties)

    feed = Streamer()
    Thread(target=feed.run).start()
    #camera_settings = properties['camera settings']
    #camera = Camera(camera_settings['id'])
    #camera.set_camera_settings(camera_settings)
    NetworkTables.initialize(server='127.0.0.1')
    r = RemoteTuner("examples/example_circle.json", my_pipeline)
    frame = cv2.imread('ball.jpg')
    while True:
        #frame = camera.get_frame()
        processed_frame = my_pipeline.process_image(frame)
        my_pipeline = r.get_pipeline()
        feed.update(processed_frame)


if __name__ == "__main__":
    main()
