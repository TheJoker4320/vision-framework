import json
import logging
import collections
import argparse

from threading import Thread
from streamer import Streamer
from camera import Camera

from pipeline.pipeline_factory import PipelineFactory
from networktables import NetworkTables
from remote_tuner import RemoteTuner


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('status')
    args = parser.parse_args()
    if args.status == '--test':
        feed = Streamer()
        Thread(target=feed.run).start()
        NetworkTables.initialize(server='10.43.20.69')

    logging.basicConfig(level=logging.INFO)

    with open("examples/example.json", "r") as file_handler:
        json_names = json.load(file_handler)
    properties = dict()  # {json name : property}
    for json_name in json_names:
        with open(json_name, "r") as file_handler:
            properties[json_name] = json.load(file_handler, object_pairs_hook=collections.OrderedDict)

    pipelines_and_cameras = dict()  # {pipeline : {}}
    for json_name, settings in properties.iteritems():
        camera_settings = settings['camera settings']
        camera = Camera(camera_settings['id'])
        camera.set_camera_settings(camera_settings)

        if args.status == '--test':
            pipeline = PipelineFactory.create_pipeline(settings)
            streamer = Streamer(json_name)
            pipelines_and_cameras[pipeline] = {'camera': camera, 'tuner': RemoteTuner(json_name, pipeline), 'streamer': streamer}
            Thread(target=streamer.run).start()
        else:
            pipelines_and_cameras[PipelineFactory.create_pipeline(settings)] = {'camera': camera}

    while True:
        for pipeline, contents in pipelines_and_cameras.iteritems():
            frame = contents['camera'].get_frame()
            processed_frame = pipeline.process_image(frame)
            if args.status == '--test':
                new_pipeline = contents['tuner'].get_pipeline()
                pipelines_and_cameras[new_pipeline] = pipelines_and_cameras.pop(pipeline)
                contents['streamer'].update(processed_frame)


if __name__ == "__main__":
    main()
