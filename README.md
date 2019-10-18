# Vision-Pipeline
The Joker's #4320 Vision Processing Framework for the First Robotics Competition (FRC). 
The code is written in python, but also uses a json format for the creation of the pipeline.

## Installation

### Requirements
* python 3.6 or higher
* opencv
* flask
* numpy
* pynetwotktables

Install all of the above libraries to run the code and then run main.py

## Code Highlights
* Built in calibration of any camera, This includes any type of a camera paramter (as long as the camera supports it).
* Verstile and easy to add new pipelines, Quirks and methodes.
* Takes about X miliseconds to build a pipeline.

## Project Philosophy
The project is based on a pipeline object.
Once you have a pipeline object you can call the pipeline's method - process_image and it will process the given image by your configurations.

The cofigurations are done in a json format, For an example see the [json example](https://github.com/TheJoker4320/vision-framework/blob/develop/examples/example.json).

### Pipeline
pipeline is a class that represents a set of operations which are preformed on an image once process_image is called. 
The following are the operations:
* modify the image.
* extract contours from the image.
* filter the extracted contours.
* calculate data from the filtered contours.
* publish data into to the Roborio. 

Every operation from the list above is represented by a class. Every implementation of this operation is a subclass of it's operation class and the pipeline applies each one of them in it's turn. see [pipeline class](https://github.com/TheJoker4320/vision-framework/blob/develop/pipeline/pipeline.py) to understand better the algorithm.

### Modifier
Modifiers is an abstract class which represents every modification that has to be preformed on the image. The modifiers are applied one after another when the result of the previous one is the input of the next one.

The modifier class has an abstract function,which is called modify. 
The modify function needs to be implemented by every subclass of modifier.
The function gets an image and returns modified image.

See [modifier class](https://github.com/TheJoker4320/vision-framework/blob/develop/modifiers/modifier.py) for more info.

### Extractor
Extractor is an abstract class which represents every extraction of contours from the modified image (from the previous operation). 
All the contours from every extractor are grouped together for the next operations.

The extractor class has an abstract function, extract. The function gets an image (the modified one from the previous stage) and returns a list of contours.

See [extractor class](https://github.com/TheJoker4320/vision-framework/blob/develop/extractors/extractor.py) for more info.

### Filter
Filter is an abstract class which represents filters that filter the contours. 
Every filter is applied on the contours (from the previous stage) and passes on only the ones that fit to the filter.
Each filter is applied on the result of the previous filter.

The filter class has an abstract function, which is called filter.
The function gets list of contours and returns list of the fit contours.

See [filter class](https://github.com/TheJoker4320/vision-framework/blob/develop/filters/filter.py) for more info.

### Calculation
Calculation is an abstract class which represents calculation that get you data from the contours from the previous stage.

The calculation class has an abstract function,calculate.The function gets list of contours, preforms the calculation and returns a dictionary with the resulted data.

See [calculation class](https://github.com/TheJoker4320/vision-framework/blob/develop/calculations/calculation.py) for more info.

### Publisher
Publisher is an abstract class which represents publishing methodologies.
Every publisher publishes data in a specific way (the data from the previous stage).

The publisher class has an abstract function, publish. The function gets a dictionary with data to publish and publishes it.

See [publish class](https://github.com/TheJoker4320/vision-framework/blob/develop/publishers/publish.py) for more info.

## Contact Info
for any problem encounterd with the Framework, feel free to contact us at our mail: frcthejoker4320@gmail.com .
