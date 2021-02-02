#  PipeLight - Vision Processing Framework
The Joker's #4320 Vision Processing Framework for the First Robotics Competition (FRC).   
The code is written entirely in Python 3, but also uses a JSON files to get user specific data for the framework.

## Table of Contents
* [Installation](#installation)
* [Code Highlights](#code-highlights)
* [Project Philosophy](#project-philosophy)
    * [Pipeline](#pipeline)
    * [Conventions](#conventions)
    * [Modification Stage](#modification-stage)
    * [Extraction Stage](#extraction-stage)
    * [Filter Stage](#filter-stage)
    * [Calculation Stage](#calculation-stage)
    * [Publishing Stage](#publishing-stage)
* [Features](#features)
    * [Pipeline Creation](#pipeline-creation)
    * [Grip File Support](#grip-file-support)
    * [Camera Calibration](#camera-calibration)
    * [Streamer](#streamer)
    * [Remote Tuner](#remote-tuner)
* [Run The Framework](#run-the-framework)
* [Credits](#credits)
* [Contact Info](#contact-info)

## Installation

### Requirements
* Python 3.6 or higher
* OpenCV (preference for version 3.4.x)
* Flask
* Numpy
* Pynetwotktables

Install all of the above libraries to run the code and then you can run main.py.  
If you don't know how to install any of the libraries check our installation guide.

### Installation Guide


3 easy step to install all the requirements (assuming you have python 3.6 and above, if not first download it):
1. *FIRST*, install the framework (you can do to it through github bash or website).
2. Open the cmd terminal in the folder.
3. Download all the requirements using the followed command:
```bash
python pip install -r requirements.txt  
```
Note: sometimes it will not find python, in that case try instated `py` or `py3` or only `pip`.


## Code Highlights
* Built in camera calibration, as long as the camera supports it.
* Very versatile framework, easy to add and manage new pipelines, Quirks and methods and functions.
* The code is open source and we highly encourage using it!
* The code was entirely written by high school students which are listed in the credits part.

## Project Philosophy
The project is based on a pipeline object.
Once you have a pipeline object you can call the main pipeline method - process_image and it will process the given image by your configurations.

### Pipeline
Pipeline is a class that represents a set of operational stages which are preformed one after the other on an image, 
which we get from the camera. All this is done once process_image is called in the main method. 

These stages include but not limited to the followings:
* Modification stage - which uses different modifiers to modify the image.
* Extraction stage - which uses different extractors to extract contours from the image.
* Filter stage - which uses different filters to filter the extracted contours.
* Calculation stage - which uses different calculations to calculate data from the filtered contours.
* Publishing stage - which uses different publishers to publish data into to the a desired machine. 

See [pipeline class](https://github.com/TheJoker4320/vision-framework/blob/develop/pipeline/pipeline.py) to better understand the algorithm that builds the pipeline.

### Conventions  
Every stage from the list above is represented by a directory.  
This directory is generally referred to as Quirks directory.  
Quirk is every file that contains a class that is used in the pipeline for any purpose.  
Each Directory contains a Main Quirk which is an abstract class, Every other class in the directory needs to implement it.  

And now here is an example:  
For the Modification Stage there is a directory called modifiers.  
This directory contains the Main Quirk which is called Modifier.  
Each and every Quirk in this directory implements it.   
For example the Blur Class implements Modifier.   

For the file conventions see the [PEP8](https://github.com/PyCQA/pep8-naming.git) convention guide.

### Modification Stage:
The first stage of the pipeline, during this stage we get a frame from the camera and apply different modifier quirks on it to get a good image for the extraction stage.

Main Quirk: modifier, see [modifier quirk](https://github.com/TheJoker4320/vision-framework/blob/develop/modifiers/modifier.py) for more info.  

Class Quirks:  
* Blur - See [blur modifier](https://github.com/TheJoker4320/vision-framework/blob/develop/modifiers/blur.py) for more info.
* Morph - See [morph modifier](https://github.com/TheJoker4320/vision-framework/blob/develop/modifiers/morph.py) for more info.
* Color Threshold - See [color threshold modifier](https://github.com/TheJoker4320/vision-framework/blob/develop/modifiers/color_threshold.py) for more info.

### Extraction Stage:
The second stage of the pipeline, during this stage we get the modified frame from the previous stage and extract all the contours from it by their type.

Main Quirk: extractor, see [extractor class](https://github.com/TheJoker4320/vision-framework/blob/develop/extractors/extractor.py) for more info.  

Class Quirks:
* Circles - See [circles_extractor class](https://github.com/TheJoker4320/vision-framework/blob/develop/extractors/circles_extractor.py) for more info.
* Simple - See [simple extractor class](https://github.com/TheJoker4320/vision-framework/blob/develop/extractors/simple_extractor.py) for more info.

### Filter Stage:
The third stage of the pipeline, during this stage we get contours from the previous stage and filter them by different parameters, like size,shape, aspect ratio and so on.

Main Quirk: filter, see [filter class](https://github.com/TheJoker4320/vision-framework/blob/develop/filters/filter.py) for more info.  

Class Quirks:
* Area Range - See [area range filter](https://github.com/TheJoker4320/vision-framework/blob/develop/filters/area_range_filter.py) for more info.
* Area Ratio - See [area ratio filter](https://github.com/TheJoker4320/vision-framework/blob/develop/filters/area_ratio_filter.py) for more info.
* Aspect Ratio - See [aspect ratio filter](https://github.com/TheJoker4320/vision-framework/blob/filters/filters/aspect_ratio_filter.py) for more info.
* Biggest Area - See [biggest area filter](https://github.com/TheJoker4320/vision-framework/blob/filters/filters/biggest_area_filter.py) for more info.
* Diagonal Pair - See [diagonal pair filter](https://github.com/TheJoker4320/vision-framework/blob/filters/filters/diagonal_reflective_tape_pair_filter.py) for more info.
* Shape - See [shape filter](https://github.com/TheJoker4320/vision-framework/blob/filters/filters/shape_filter.py) for more info.

### Calculation Stage:
The fourth stage of the pipeline, during this stage we use the different filtered contours from the previous stage for many different calculations, these include distance and angle calculations for every filtered contour.

Main Quirk: calculation, see [calculation class](https://github.com/TheJoker4320/vision-framework/blob/develop/calculations/modifier.py) for more info.  

Class Quirks:
* Angle - See [angle calculation](https://github.com/TheJoker4320/vision-framework/blob/develop/calculations/angle_calculation.py) for more info.
* more will be added soon!

### Publishing Stage:
The last stage of the pipeline, during this stage we send (publish) the calculations from the previous stage to the desired Robot, Computer or any other working machine that can run python.

Main Quirk: publisher, see [publisher class](https://github.com/TheJoker4320/vision-framework/blob/develop/publishers/publish.py) for more info.  
 
Class Quirks:
* Logging Publisher - See [logging class](https://github.com/TheJoker4320/vision-framework/blob/develop/publishers/logging_publisher.py) for more info.
* Network Table Publisher - See [network table class](https://github.com/TheJoker4320/vision-framework/blob/develop/publishers/network_table_publisher.py) for more info.

## Features

### Pipeline Creation
The framework uses a json file as a way of creating a pipeline.  
For an example file you see can check the [examples directory](https://github.com/TheJoker4320/vision-framework/blob/develop/examples).                  

We highly recommend you will be familiar with JSON before trying to create a pipeline.

The framework support now several Quirks as written above and you can already use them on your vision pipeline.  

Note: the order of each the Quirks in each stage is according to the order in the JSON file.

#### Modification Stage

|Quirk Name|Variables|type|Description|Code Link|
|----------|---------|----|-----------|---------|
|Blur      |kernel - the size of the kernel across the x and y axises of the image, the height and width should be odd| list of 2 floats (convert to tuple in the program). | Blurs the image using a blur kernel.|[blur modifier](https://github.com/TheJoker4320/vision-framework/blob/develop/modifiers/blur.py)|
|ColorThreshold|low_h - the lower limit of the Hue range <br> low_s - the lower limit of the Saturation range <br> low_v - the lower limit of the Value range <br> high_h - the higher limit of the Hue range<br> high_s - the higher limit of the Saturation range <br> high_v - the higher limit of the value range <br> do_mask - flag for performing mask|hsv values - float <br> do_mask - boolean|Applies color threshold using HSV <br> Can perform mask, via bitwise AND operation, between the original frame and the HSV.|[color threshold modifier](https://github.com/TheJoker4320/vision-framework/blob/develop/modifiers/color_threshold.py)|
|Morph|morph_open - the size of the kernel for the Opening<br> morph_close - the size of the kernel for the Closing | list of 2 floats (convert to a numpy array in the program)|Applies either open, close, both open and close or none of them on a frame.|[morph modifier](https://github.com/TheJoker4320/vision-framework/blob/develop/modifiers/morph.py)|


And how it look on the json file (all of the modifiers above, you can delete what you do not want to use)  
Example in the JSON file:

```python 
{ 
    "modifiers": { 
    
        "Blur": {
            "kernel": [
                5,
                5
            ]
        },
            
        "ColorThreshold": {
            "do_mask": true,
            "high_h": 84,
            "high_s": 255,
            "high_v": 103,
            "low_h": 63,
            "low_s": 209,
            "low_v": 29
        },
            
        "Morph": {
            "morph_close": [
                5,
                5
            ],
            "morph_open": [
                5,
                5
            ]
        }
    },
    ...
}
```
Note that except of the last one all of them has , after (to understand why it is highly recommended to read JSON file format).

#### Extraction Stage
|Quirk Name|Variables|type|Description|Code Link|
|----------|---------|----|-----------|---------|
|SimpleExtractor|None| None| Extracts all the contours that were detected at the given frame.|[simple extractor class](https://github.com/TheJoker4320/vision-framework/blob/develop/extractors/simple_extractor.py)|
|CirclesExtractor|dp - This parameter is the inverse ratio of the accumulator resolution to the image resolution (see Yuen et al. for more details). Essentially, the larger the dp gets, the smaller the accumulator array gets <br> minimum_distance - Minimum distance between the center (x, y) coordinates of detected circles. If the distance is too small, multiple circles in the same neighborhood as the original may be (falsely) detected. If the distance is too large, then some circles may not be detected at all| float | Extracts all the contours that are circular.|[circles_extractor class](https://github.com/TheJoker4320/vision-framework/blob/develop/extractors/circles_extractor.py)|

And how it look on the json file (all of the extractors above, you can delete what you do not want to use)  
Example in the JSON file:

```python 
{ 
    "extractors": {
    
        "SimpleExtractor": {},
        
        "CirclesExtractor": {
            "dp": 2.072649572649573, 
            "minimum_distance": 75.0
        }
    },
    ...
}
```
Note that except of the last one all of them has , after (to understand why it is highly recommended to read JSON file format).

#### Filter Stage
|Quirk Name|Variables|type|Description|Code Link|
|----------|---------|----|-----------|---------|
|AreaRangeFilter|min_area - the minimum area of the contour to filter <br> max_area - the maximum area of the contour to filter|float| Filters the contours by minimum and maximum values of the area. <br> The area is defined by the contour area.|[area range filter](https://github.com/TheJoker4320/vision-framework/blob/develop/filters/area_range_filter.py)|
|AreaRatioFilter|min_area_ratio - the minimum area ratio of the contour to filter <br> max_area_ratio - the maximum area ratio of the contour to filter|float| Filters the contours by minimum and maximum values of the area ratio. <br> The area ratio is defined as the ratio between the rectangle area and contour area.|[area ratio filter](https://github.com/TheJoker4320/vision-framework/blob/develop/filters/area_ratio_filter.py)|
|AspectRatioFilter| min_ratio - the minimum aspect ratio of the contour to filter <br> max_ratio - the maximum aspect ratio of the contour to filter|float| Filters the contours by minimum and maximum values of the aspect ratio. <br> The aspect ratio defined as the ratio between the height and width. <br> Height defined as the longer between the two side's length.|[aspect ratio filter](https://github.com/TheJoker4320/vision-framework/blob/filters/filters/aspect_ratio_filter.py) |
|BiggestAreaFilter|None|None| Goes over all the contours and returns the one with the biggest area.|[biggest area filter](https://github.com/TheJoker4320/vision-framework/blob/filters/filters/biggest_area_filter.py)|
|DiagonalReflectiveTapePair|None|None| Goes over all the contours returns the two that turn to each other. <br> Matches to the 2019 requirements.|[diagonal pair filter](https://github.com/TheJoker4320/vision-framework/blob/filters/filters/diagonal_reflective_tape_pair_filter.py)|
|ShapeFilter| edges_count - the number of edges <br> epsilon - the value which is used to approximate the shape type| edges_count - int <br> epsilon - float| Filters the contours by their approximate shape. <br> Checks the approximate shape according to epsilon value. <br> As epsilon is bigger the filtering is more flexible.|[shape filter](https://github.com/TheJoker4320/vision-framework/blob/filters/filters/shape_filter.py)|

And how it look on the json file (all of the filters above, you can delete what you do not want to use)  
Example in the JSON file:

```python 
{ 
    "filters": {
    
        "AreaRangeFilter": {
            "min_area": 100,
            "max_area": 60000
        },
        
        "AreaRatioFilter": {
            "min_area_ratio": 0.8,
            "max_area_ratio": 1
        },
        
        "AspectRatioFilter": {
            "min_ratio": 0.12345679012345678,
            "max_ratio": 8.1
        },
        
        "BiggestAreaFilter": {},
        
        "DiagonalReflectiveTapePair": {},
        
        "ShapeFilter": {
            "edges_count": 4,
            "epsilon": 0.8
        }
    },
    ...
}
```
Note that except of the last one all of them has , after (to understand why it is highly recommended to read JSON file format).

#### Calculation Stage
|Quirk Name|Variables|type|Description|Code Link|
|----------|---------|----|-----------|---------|
|AngleCalculation|image_width - the width of the image (in pixels) <br> horizontal_field_of_view - the field of view on the horizontal axis (in degrees) <br> image_x_center - the image x center <br> image_y_center - the image y center|float|Calculate the x and y angels between the camera and the object in the image.|[angle calculation](https://github.com/TheJoker4320/vision-framework/blob/develop/calculations/angle_calculation.py)|
|DistanceCalculationByArea| field_of_view - the fov of the camera (in degrees) <br> image_width - the width of the image (in pixels) <br> real_area - the real area of the object| float| Calculates the distance between the camera and the object.|[distance calculation by area calculation](https://github.com/TheJoker4320/vision-framework/blob/develop/calculations/distance_calculation_by_area.py)|
|DistanceCalculationByFocalLength| field_of_view - the fov of the camera (in degrees) <br> image_width - the width of the image (in pixels) <br> real_height - the real height of the object (in meters)| float| Calculates the distance between the camera and the object.|[distance calculation by focal length calculation](https://github.com/TheJoker4320/vision-framework/blob/develop/calculations/distance_calculation_by_focal_length.py)|
|DistanceCalculationByFunction| distance_function - self made distance calculation function, where f(x) is the real distance of the camera from the object and x is the image's height in pixels (imaginary_height)| str| Calculates the distance between the camera and the object.|[distance calculation by function calculation](https://github.com/TheJoker4320/vision-framework/blob/develop/calculations/distance_calculation_by_function.py)|
|DistanceCalculationByVector| horizontal_field_of_view - the field of view on the horizontal axis (in degrees) <br> vertical_field_of_view - the field of view on the vertical axis (in degrees) <br> image_width - the width of the image (in pixels) <br> image_height - the height of the image (in pixels) <br> object_surface_area - the object surface area (in meters ** 2) <br> yaw_angle - the clockwise yaw angle (in degrees) in which the camera is rotated, the yaw angle is the angle around the y axis (default is 0.0) <br> pitch_angle - the clockwise pitch angle (in degrees) in which the camera is rotated, the pitch angle is the angle around the x axis (default is 0.0) <br> roll_angle - the clockwise roll angle (in degrees) in which the camera is rotated, the roll angle is the angle around the z axis (default is 0.0) <br> x_offset - the distance (in meters) in the x axis away from the center of the robot (default is 0.0) <br> y_offset - the distance (in meters) in the y axis away from the center of the robot (default is 0.0) <br> z_offset - the distance (in meters) in the z axis away from the center of the robot (default is 0.0)| float| Calculates the distance between the camera and the object across the x, y and z axises.|[distance calculation by vector calculation](https://github.com/TheJoker4320/vision-framework/blob/develop/calculations/distance_calculation_by_vector.py)|
|TurnCalculation| field_of_view - the fov of the camera (in degrees) <br> image_width - the width of the image (in pixels) <br> real_height - the real height of the object (in meters) <br> tape_width - the diagonal reflective tape's width (in meters)| float| Calculate the distance of the 2 edges of a triangle (those are the two relevant distance) and the third edge is the direct distance, and calculate the angle needed to turn to get to the first edge's position. <br> Matches to the 2019 requirements|[turn calculation](https://github.com/TheJoker4320/vision-framework/blob/develop/calculations/turn_calculation.py)|
   
And how it look on the json file (all of the calculations above, you can delete what you do not want to use)  
Example in the JSON file:

```python 
{ 
    "calculations": {
    
        "AngleCalculation": {
            "image_x_center": 319,
            "horizontal_field_of_view": 48.068,
            "image_width": 640,
            "image_y_center": 239
        },
        
        "DistanceCalculationByArea": {
            "field_of_view": 48.02,
            "image_width": 640,
            "real_area": 0.2205
        },
        
        "DistanceCalculationByFocalLength": {
            "field_of_view": 48.02,
            "image_width": 640,
            "real_height": 0.65
        },
        
        "DistanceCalculationByFunction": {
            "distance_function": "193.1*(imaginary_height**0.934)"
        },
        
        "DistanceCalculationByVector": {
            "horizontal_field_of_view": 48.068,
            "vertical_field_of_view": 36.051,
            "image_width": 640,
            "image_height": 480,
            "object_surface_area": 0.327599,
            "yaw_angle": 0.0,
            "pitch_angle": 0.0,
            "roll_angle": 0.0,
            "x_offset": 0.0,
            "y_offset": 0.0,
            "z_offset": 0.0
        },
        
        "TurnCalculation": {
            "field_of_view": 48.02,
            "image_width": 640,
            "real_height": 20.32,
            "tape_width": 12.7
        }
    },
    ...
}
```
Note that except of the last one all of them has , after (to understand why it is highly recommended to read JSON file format).


#### Publishing Stage
|Quirk Name|Variables|type|Description|Code Link|
|----------|---------|----|-----------|---------|
|LoggingPublisher|None|None| A publish class. Responsible for logging the information at info level.|[logging class](https://github.com/TheJoker4320/vision-framework/blob/develop/publishers/logging_publisher.py)|
|NetworkTablePublisher| table_name - the name of the network table to publish to <br> team_num - the number of the team| table_name - str <br> team_num - int (but can get float)| Publish the calculated data to the specified table via network tables protocol.|[network table class](https://github.com/TheJoker4320/vision-framework/blob/develop/publishers/network_table_publisher.py)|

And how it look on the json file (all of the publishers above, you can delete what you do not want to use)  
Example in the JSON file:

```python 
{ 
    "publishers": {
    
        "LoggingPublisher": {},
        
        "NetworkTablePublisher": {
            "table_name": "SmartDashboard", 
            "team_num": 4320
        }
    },
    ...
}
```
Note that except of the last one all of them has , after (to understand why it is highly recommended to read JSON file format).

### Grip File Support
We as a framework offer the users to convert a GRIP file to JSON file.  
The converter is also versatile and need to be update according to the GRIP program and the framework development.  
to convert a GRIP file to JSON file all you need is to:
1. create a grip file
2. create a basic JSON file - a JSON file that contain the basic format for the framework (you can find one in the examples directory as [example.py](https://github.com/TheJoker4320/vision-framework/blob/develop/examples/example.py).       )
3. run on the command line the followed command:  
```bash 
python convert_grip_to_json.py grip_file_name.grip json_file_name.json
```

If you want to add more support to the converter or just check comment about the function you can see the [converter](https://github.com/TheJoker4320/vision-framework/blob/develop/convert_grip_to_json.py) and edit it in the designated place.

### Camera Calibration
The Camera calibration is done by writing all the camera parameters that you want to calibrate in a JSON file format (where you write your pipeline creation input). Then all the parameters are given to camera.py, and that calibrates them.  
For the camera calibration v4l2 is used (make sure you have it)
if you do not have it all you need to is write the followed command in the command line:
```bash
$ sudo apt-get update

$ sudo apt-get install v4l-utils
```
As you can see it can only be done on a linux based system (v4l2 - Video4Linux version 2) such on the FIRST operation system to the raspberry pi or the basic os of the jetson.  

The camera parameters includes:
* brightness (int) - Picture brightness, or more precisely, the black level (int).
* contrast (int) - Picture contrast or luma gain (int).
* saturation (int) - Picture color saturation or chroma gain (int).
* white balance temperature auto (0 or 1 - bool but as an int) - Automatic white balance.
* power line frequency (int) - Enables a power line frequency filter to avoid flicker. Possible values for it is 0-3.
* white balance temperature (int) - This control specifies the white balance settings as a color temperature in Kelvin. A driver should have a minimum of 2800 (incandescent) to 6500 (daylight). 
* sharpness (int) - Adjusts the sharpness filters in a camera. The minimum value disables the filters, higher values give a sharper picture. 
* backlight compensation (int) - Adjusts the backlight compensation in a camera. The minimum value disables backlight compensation.
* exposure auto (int) - Enables automatic adjustments of the exposure time and/or iris aperture. The effect of manual changes of the exposure time or iris aperture while these features are enabled is undefined, drivers should ignore such requests. Possible values are 0-3
* exposure absolute (int) - Determines the exposure time of the camera sensor. The exposure time is limited by the frame interval. Drivers should interpret the values as 100 µs units, where the value 1 stands for 1/10000th of a second, 10000 for 1 second and 100000 for 10 seconds.
* pan absolute (int) - This control turns the camera horizontally to the specified position. Positive values move the camera to the right (clockwise when viewed from above), negative values to the left. Drivers should interpret the values as arc seconds, with valid values between -180 * 3600 and +180 * 3600 inclusive.
* tilt absolute (int) - This control turns the camera vertically to the specified position. Positive values move the camera up, negative values down. Drivers should interpret the values as arc seconds, with valid values between -180 * 3600 and +180 * 3600 inclusive.
* zoom absolute (int) - Specify the objective lens focal length as an absolute value. The zoom unit is driver-specific and its value should be a positive integer.

for more information about this setting and more see this [link](https://www.kernel.org/doc/html/latest/userspace-api/media/v4l/ext-ctrls-camera.html)

Another important thing is the id of the camera and the field of view that is also included in the JSON file:
The id is the port that the camera connect to (if it is the first camera it is 0 the second is 1, it is relevant to how much cameras connected and not to the place of the port).  
The field of view is the field of view of the camera.  

And how it look on the json file (all of the parameters above, you can delete what you do not want to use)  
Example in the JSON file:

```python
{
    "camera settings": {
        "white balance temperature auto": 0,
        "saturation": 100,
        "brightness": 70,
        "backlight compensation": 0,
        "sharpness": 25,
        "power line frequency": 2,
        "white balance temperature": 4500,
        "pan absolute": 0,
        "field of view": 68.5,
        "exposure absolute": 5,
        "tilt absolute": 0,
        "exposure auto": 1,
        "contrast": 10,
        "zoom absolute": 0,
        "id": 0
      }
}
```

To learn more about this process check [camera class](https://github.com/TheJoker4320/vision-framework/blob/develop/camera.py).

### Streamer 

One of the features in the framework is the Streamer that allows the user to watch live feed of the vision processing.  
all you need to do is to enter the location of the JSON file (build in format of the framework) and it will open a stream to your local network where the feed is at the location of ip where the code is running from + the JSON file name.  
for an example your computer ip is 10.43.20.10 and your json file name is example.json then the location of the stream is at 10.43.20.10/example and you can watch the feed through your browser.  

To use the streamer in the code, you need to add to the main file (see why on the next topic on [running the framework](#run-the-framework))
first, you need to create an Streamer as an object:
```python
from streamer import Streamer

# Create a streamer
streamer = Streamer(json_file_path)
```

you need to put the stream on a thread to make sure it will not block stuck your program:
```python
# Start stream
Thread(target=Streamer.run).start()
```

afterward you need to get a frame (the pre-process or pro-process, an image you would like to stream), at this case we will take a `processed_frame` variable to be the frame and now we just need to stream it:
```python
# Update the streamer with the processed frame
streamer.update(processed_frame)
```
Note: the `streamer.update(processed_frame)` suppose to be in the loop if you want it to make a video stream (you can see an example of the streamer in main in the topic about [running the framework](#run-the-framework)).

To learn more about this feature check [streamer class](https://github.com/TheJoker4320/vision-framework/blob/develop/streamer.py).
### Remote Tuner

The Remote Tuner is another feature our framework contains which allow the user to tune the values in the used json file remotely.  
all you need to do is run the main.py with the tuner object and excess it through the outline viewer program (this is one of FIRST programs),
after you have done this you will see the JSON file name as a table name you you will be able to tune the values in it and it will automatically update the JSON file and the pipeline                                                   

To use the remote tuner in the code, you need to add to the main file (see why on the next topic on [running the framework](#run-the-framework)), notice you need to add `json_file_path` and `my_pipeline` means you have to create a pipeline and add his JSON file location the class initializer.
first, you need to create an Remote_Tuner as an object:
```python
from remote_tuner import RemoteTuner

# Create a remote tuner
tuner = RemoteTuner(json_file_path, my_pipeline)
```

afterward you need to get the pipeline (if value is changing the tuner creates a new pipeline otherwise its the same one), at this case we set the `my_pipeline` variable to be the relevant pipeline:
```python
# Update the pipeline (if any value in the tuner changed)
my_pipeline = tuner.get_pipeline()
```
Note: the `my_pipeline = tuner.get_pipeline()` suppose to be in the loop if you want to always be able to update the pipeline (you can see an example of the streamer in main in the topic about [running the framework](#run-the-framework)).

To learn more about this feature check [remote tuner class](https://github.com/TheJoker4320/vision-framework/blob/develop/remote_tuner.py).

## Run The Framework
To run the framework all you need to do is run the `main.py` file, but do not forget to update it according to your need.  
The main file contains:  
* The pipeline creation according to the inserted JSON file.
* The camera calibration according to the inserted JSON file.
* A stream of the processed video (can be on a comment on a game)
* A remote tuner for the JSON file (can be on a comment on a game)

Example of a simple main file:
```python
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
    # Start logging
    logging.basicConfig(level=logging.INFO)
    
    # Set the JSON file for the pipeline 
    json_file_path = "examples/example.json"
    
    # Open the JSON file and read the data
    with open(json_file_path, "r") as file_handler:
        properties = json.load(file_handler, object_pairs_hook=collections.OrderedDict)
    # Create a pipeline according to the properties
    my_pipeline = PipelineFactory.create_pipeline(properties)
    
    # Get the camera setting
    camera_settings = properties['camera settings']
    # Create a camera 
    camera = Camera(camera_settings['id'], cv2.CAP_V4L)
    # Set the camera setting (the wanted calibration and etc.)
    camera.set_camera_settings(camera_settings)
    
    # Create a remote tuner
    tuner = RemoteTuner(json_file_path, my_pipeline)
    
    # Create a streamer
    streamer = Streamer(json_file_path)
    # Start stream
    Thread(target=Streamer.run).start()

    while True:
        # Get frame from the camera
        frame = camera.get_frame()
        # Process it according to the pipeline
        processed_frame = my_pipeline.process_image(frame)
        # Update the streamer with the processed frame
        streamer.update(processed_frame)
        # Update the pipeline (if any value in the tuner changed)
        my_pipeline = tuner.get_pipeline()


if __name__ == "__main__":
    main()
```

You can modify the main to match your vision need - number of cameras, multiple pipelines, stream or tune need and more. 

## Credits
Original Vision Processing team which includes (2018-2019):
* Zohar Shaked
* Shay Linzberg 
* Bar-Hen Krochmel  
  
Code Contributors:  
* Nadav Moran  
  
Special thanks to:       
Daniel Vaserstein - For helping us organize our code better, helping set the project conventions and mentoring us till the very end.

## Contact Info
For any problem encountered with the Framework, feel free to contact us at our mail: frcthejoker4320@gmail.com  
or just write us a issue in this branch.
