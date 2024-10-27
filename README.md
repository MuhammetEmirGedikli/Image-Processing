Image Processing Projects
This repository contains various image processing projects developed using OpenCV and NumPy. The purpose of these projects is to apply and analyze different image processing techniques. Each project includes an independent Python script that accomplishes a specific task.

Technologies Used:

Python
OpenCV: For image processing and analysis
NumPy: For mathematical operations and data processing
Projects
The projects included in this repository cover:

Object Detection: Face detection and object recognition.
Distance Calculation from Camera: Using the height of an object in an image to calculate the distance between the camera and the object.
Distance Calculation from Camera using OpenCV
This project estimates the distance between a camera and an object by analyzing the object's size within an image. By using OpenCV, we can detect the object, measure its dimensions in pixels, and then apply a mathematical formula to determine its distance from the camera.

How It Works
Load the Image: The script starts by loading an image with the target object.

Object Detection: Using OpenCV's built-in classifiers (e.g., for face detection), the script identifies the object in the image and measures its height in pixels.

Distance Calculation: Based on the camera’s focal length and the known real-world height of the object, the script calculates the distance between the camera and the object using the following formula:

Distance = Focal Length × Real Object Height / Object Height in Pixels​
 
Result Visualization: The calculated distance is displayed on the image itself, making it easy to verify and visualize the output.

Requirements:
Python
OpenCV
NumPy


Setup & Run Instructions:

git clone https://github.com/MuhammetEmirGedikli/distancecalculating.git
cd distancecalculating

Install dependencies:

pip install -r requirements.txt


Run the script:

python distance_calculation.py

This project is a useful foundation for applications in robotics, augmented reality, and automated measurements, where distance estimation is a crucial requirement.
