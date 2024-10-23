****Camera.py***

# Real-Time Webcam Feed Viewer

This project captures live video from a webcam and displays it in a window using OpenCV.

## Requirements

- Python 3.x
- OpenCV

You can install the required package using pip:

```bash
pip install opencv-python
Code Explanation
Setup: The necessary library (OpenCV) is imported, and the webcam is opened for video capture.

Webcam Check: The code checks if the webcam is successfully opened. If not, it raises an error.

Video Processing Loop:

The program continuously captures frames from the webcam.
Each frame is resized to 50% of its original dimensions for easier viewing.
The resized frame is displayed in a window titled "Input".
Exit Condition: The loop continues until the 'q' key is pressed, at which point the program terminates.

Usage
Run the script, and a window will open displaying the webcam feed. Press 'q' to exit.

Purpose
The purpose of this code is to demonstrate a simple real-time video feed viewer using a webcam, highlighting basic video capture and display techniques with OpenCV.





***face.detection.py***


# Real-Time Face Detection using OpenCV and MediaPipe

This project captures live video from a webcam and performs real-time face detection using OpenCV and MediaPipe. It identifies faces in the video feed and draws bounding boxes around them.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe

You can install the required packages using pip:

```bash
pip install opencv-python mediapipe
Code Explanation
Setup: The necessary libraries are imported, and the webcam is opened for video capture.

Face Detection Initialization: The face detection model is initialized with a specified confidence threshold of 20%.

Video Processing Loop:

The program continuously captures frames from the webcam.
Each frame is processed to detect faces.
Bounding boxes are drawn around detected faces.
Exit Condition: The loop continues until the 'q' key is pressed, at which point the program terminates.

Usage
Run the script, and a window will open displaying the webcam feed. Press 'q' to exit.

Purpose
The purpose of this code is to demonstrate a simple real-time face detection application using a webcam, showcasing the capabilities of OpenCV and MediaPipe for detecting and highlighting faces in video streams.




***hand.detection***


# Hand Gesture Recognition

This project utilizes MediaPipe to detect and recognize hand gestures in real-time via a webcam.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe

You can install the required packages using pip:

```bash
pip install opencv-python mediapipe
Code Explanation
Setup: The necessary libraries (OpenCV and MediaPipe) are imported, and the webcam is initialized with a resolution of 640x480.

Hand Detection: The MediaPipe Hands module is used to detect hand landmarks in the captured video frames.

Landmark Processing:

The program captures frames from the webcam and converts them to RGB for processing.
It checks if any hands are detected and draws landmarks and connections on the image.
Finger Counting Logic:

The program determines whether the detected hand is the left or right based on the position of specific landmarks (tip of the thumb).
It counts how many fingers are raised by comparing the positions of the finger tips to their corresponding joints.
Display: The total number of fingers raised is displayed on the screen.

Usage
Run the script, and a window will open showing the webcam feed. The program will indicate whether the left or right hand is detected and display the count of raised fingers. Press 'q' to exit.

Purpose
The purpose of this code is to demonstrate real-time hand gesture recognition using MediaPipe, showcasing the detection of hand positions and counting the number of fingers raised.





