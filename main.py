import json
from pipeline.pipeline_factory import PipelineFactory
import logging
from camera import Camera


def main():
    logging.basicConfig(level=logging.INFO)
    camera = Camera(1)
    with open("jak.json", "r") as f:
        prop = json.load(f)
    my_pipeline = PipelineFactory.create_pipeline(prop)
    while True:
        my_pipeline.process_image(camera.get_frame())


if __name__ == "__main__":
    main()
