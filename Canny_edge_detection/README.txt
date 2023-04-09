Canny Edge Detection
This code uses the Canny edge detection algorithm to detect edges in an input image. It reads an input image, resizes it to a fixed size of 600x600 pixels, and then applies the Canny edge detection algorithm on the grayscale version of the image.

Dependencies
This code requires the following dependencies:

OpenCV (cv2)
Usage
To run the code, save an input image as 01.png in the same directory as the script. Then, run the script with the following command:

python
Copy code
python canny_edge_detection.py
This will display three windows with the following images:

Original: the original input image
Grayscale: the grayscale version of the input image
Edges: the edges detected in the input image using the Canny edge detection algorithm
The resulting grayscale and edges images are also saved as gray_output.png and canny.png, respectively, in the same directory as the script.

Parameters
The Canny edge detection algorithm has two threshold values that can be adjusted to control the edge detection. In this code, the low and high threshold values are set to 60 and 120, respectively. These values can be adjusted by modifying the low_threshold and high_threshold variables in the script.

Window size
The window size for displaying the images has been set to a fixed size of 600x600 pixels using the win_size variable in the script. This can be adjusted to a different size if desired.

Author
This code was written by Tilak Parajuli.
