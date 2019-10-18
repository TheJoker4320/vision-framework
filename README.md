# Vision-Pipeline
The Joker's #4320 Vision Processing Framework for the First Robotics Competition (FRC).   
The code is written entirely in Python 3, but also uses a json files to get user specific data for the creation of the pipeline.

## Installation

### Requirements
* Python 3.6 or higher
* OpenCV
* Flask
* Numpy
* Pynetwotktables

Install all of the above libraries to run the code and then run main.py

## Code Highlights
* Built in calibration of any camera, This includes any type of a camera paramter (as long as the camera supports it).
* Very verstile framework, It is easy to add new pipelines, Quirks and methods.
* Takes about X miliseconds to build a pipeline.
* The code was entirely written by high school students which are listed in the credits part.

## Project Philosophy
The project is based on a pipeline object.
Once you have a pipeline object you can call the main pipeline method - process_image and it will process the given image by your configurations.

The cofigurations are done in a json format, For an example see the [json example](https://github.com/TheJoker4320/vision-framework/blob/develop/examples/example.json).

### Pipeline
Pipeline is a class that represents a set of operational stages which are preformed one after the other on an image, 
which we get from the camera. All this is done once process_image is called in the main methoed. 

These stages inculde but not limted to the followings:
* Modification stage - which uses diffrent modifiers to modify the image.
* Extraction stage - which uses diffrent extractors to extract contours from the image.
* Filter stage - which uses diffrent filters to filter the extracted contours.
* Calculation stage - which uses diffrent calculations to calculate data from the filtered contours.
* Publishing stage - which uses diffrent publishers to publish data into to the a desired machine. 

Every stage from the list above is represented by a directory. 
Each Directory contains a "Main Quirk" which is an abstract class.
Each and every implementation of the "Main Quirk" is called a Quirk.

Here is an example:
For the modification stage there is a directory called modifiers. 
This directory contains the "Main Quirk" which is called modifer.
Each and every Quirk (file) in this directory implements The Main Quirk. 
For example the Blur Quirk (object) implements the Modifier which is the Main Quirk (object). 

See [pipeline class](https://github.com/TheJoker4320/vision-framework/blob/develop/pipeline/pipeline.py) to better understand the algorithm that builds the pipeline.

### Modification Stage
The first stage of the pipeline, during this stage we get a frame from the camera and applie diffrent modifier quirks on it to get a good image for the extraction stage.

Main Quirk: modifier, see [modifier class](https://github.com/TheJoker4320/vision-framework/blob/develop/modifiers/modifier.py) for more info.  
Class Quirks:
* Blur - See [blur class](https://github.com/TheJoker4320/vision-framework/blob/develop/modifiers/blur.py) for info
* Morph - See [morph class](https://github.com/TheJoker4320/vision-framework/blob/develop/modifiers/morph.py) for info
* Color Treshold - See [blur class](https://github.com/TheJoker4320/vision-framework/blob/develop/modifiers/color_threshold.py) for info


### Extraction Stage
Extractor is an abstract class which represents every extraction of contours from the modified image (from the previous operation). 
All the contours from every extractor are grouped together for the next operations.

The extractor class has an abstract function, extract. The function gets an image (the modified one from the previous stage) and returns a list of contours.

See [extractor class](https://github.com/TheJoker4320/vision-framework/blob/develop/extractors/extractor.py) for more info.

### Filter Stage
Filter is an abstract class which represents filters that filter the contours. 
Every filter is applied on the contours (from the previous stage) and passes on only the ones that fit to the filter.
Each filter is applied on the result of the previous filter.

The filter class has an abstract function, which is called filter.
The function gets list of contours and returns list of the fit contours.

See [filter class](https://github.com/TheJoker4320/vision-framework/blob/develop/filters/filter.py) for more info.

### Calculation Stage
Calculation is an abstract class which represents calculation that get you data from the contours from the previous stage.

The calculation class has an abstract function,calculate.The function gets list of contours, preforms the calculation and returns a dictionary with the resulted data.

See [calculation class](https://github.com/TheJoker4320/vision-framework/blob/develop/calculations/calculation.py) for more info.

### Publishing Stage
Publisher is an abstract class which represents publishing methodologies.
Every publisher publishes data in a specific way (the data from the previous stage).

The publisher class has an abstract function, publish. The function gets a dictionary with data to publish and publishes it.

See [publish class](https://github.com/TheJoker4320/vision-framework/blob/develop/publishers/publish.py) for more info.

## Conventions

## Credits
WIP

## Contact Info
For any problem encounterd with the Framework, feel free to contact us at our mail: frcthejoker4320@gmail.com .
