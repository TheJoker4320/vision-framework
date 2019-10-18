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

## Project Conventions
Every stage from the list above is represented by a directory and is called the <quirk>s. 
Each Directory contains a "Main Quirk" which is an abstract class and is called <quirk>.
Each and every implementation of the "Main Quirk" is given a name for example <quirk> a.

And now here is an example:
For the modification stage there is a directory called modifiers. 
This directory contains the "Main Quirk" which is called modifer.
Each and every Quirk (file) in this directory implements The Ma in Quirk. 
For example the Blur Quirk (object) implements the Modifier which is the Main Quirk (object). 

See [pipeline class](https://github.com/TheJoker4320/vision-framework/blob/develop/pipeline/pipeline.py) to better understand the algorithm that builds the pipeline.

### Modification Stage:
The first stage of the pipeline, during this stage we get a frame from the camera and applie diffrent modifier quirks on it to get a good image for the extraction stage.

Main Quirk: modifier, see [modifier quirk](https://github.com/TheJoker4320/vision-framework/blob/develop/modifiers/modifier.py) for more info.  

Class Quirks:
* Blur - See [blur modifier](https://github.com/TheJoker4320/vision-framework/blob/develop/modifiers/blur.py) for more info.
* Morph - See [morph modifier](https://github.com/TheJoker4320/vision-framework/blob/develop/modifiers/morph.py) for more info.
* Color Treshold - See [color treshold modifier](https://github.com/TheJoker4320/vision-framework/blob/develop/modifiers/color_threshold.py) for more info.


### Extraction Stage:
The second stage of the pipeline, during this stage we get the modified frame from the previous stage and extract all the contours from it by their type.

Main Quirk: extractor, see [extractor class](https://github.com/TheJoker4320/vision-framework/blob/develop/extractors/extractor.py) for more info.  

Class Quirks:
* Circles - See [circles_extractor class](https://github.com/TheJoker4320/vision-framework/blob/develop/extractors/circles_extractor.py) for more info.
* Simple - See [simple extractor class](https://github.com/TheJoker4320/vision-framework/blob/develop/extractors/simple_extractor.py) for more info.


### Filter Stage:
The third stage of the pipeline, during this stage we get contours from the previous stage and filter them by diffrent parameters, like size,shape, aspect ratio and so on.

Main Quirk: filter, see [filter class](https://github.com/TheJoker4320/vision-framework/blob/develop/filters/filter.py) for more info.  

Class Quirks:
* Area Range - See [area range filter](https://github.com/TheJoker4320/vision-framework/blob/develop/filters/area_range_filter.py) for more info.
* Area Ratio - See [area ratio filter](https://github.com/TheJoker4320/vision-framework/blob/develop/filters/area_ratio_filter.py) for more info.
* Aspect Ratio - See [aspect ratio filter](https://github.com/TheJoker4320/vision-framework/blob/filters/filters/aspect_ratio_filter.py) for more info.
* Biggest Area - See [biggest area filter](https://github.com/TheJoker4320/vision-framework/blob/filters/filters/biggest_area_filter.py) for more info.
* Diagonal Reflective Tape - See [diagonal reflective tape pair filter](https://github.com/TheJoker4320/vision-framework/blob/filters/filters/diagonal_reflective_tape_pair_filter.py) for more info.
* Shpae - See [shape filter](https://github.com/TheJoker4320/vision-framework/blob/filters/filters/shape_filter.py) for more info.

### Calculation Stage:
The fourth stage of the pipeline, during this stage we use the diffrent filtered contours from the previous stage for many diffrent calculations, these inculde distance and angle calcualtions for every filterd contour.

Main Quirk: calculation, see [calculation class](https://github.com/TheJoker4320/vision-framework/blob/develop/calculations/modifier.py) for more info.  

Class Quirks:
* Angle - See [angle calculation](https://github.com/TheJoker4320/vision-framework/blob/develop/calculations/angle_calculation.py) for more info.
* more will be added soon!

### Publishing Stage:
The last stage of the pipeline, during this stage we send (publish) the calcultaions from the previous stage to the desired Robot, Computer or any other working machine that can run python.

Main Quirk: publisher, see [publisher class](https://github.com/TheJoker4320/vision-framework/blob/develop/publishers/publish.py) for more info.  
Class Quirks:
* Logging Publisher - See [logging class](https://github.com/TheJoker4320/vision-framework/blob/develop/publishers/logging_publisher.py) for more info.
* Network Table Publisher - See [morph class](https://github.com/TheJoker4320/vision-framework/blob/develop/publishers/network_table_publisher.py) for more info.

### Pipeline Creation
The framework uses a json file as a way of creating a pipeline.  
For an example file you see can check the [examples directory](https://github.com/TheJoker4320/vision-framework/blob/develop/examples)

## Credits
Original Vision Proccessing team which inculdes (2019-2020):
* Zohar Shaked
* Shay Linzberg 
* Nadav Moran
* Bar-Hen Krochmel

Special thanks to:       
Daniel Vaserstein - For helping us organize our code better, helping set the project conventions and mentoring us till the very end.

## Contact Info
For any problem encounterd with the Framework, feel free to contact us at our mail: frcthejoker4320@gmail.com  
or just write us a issue in this branch.
