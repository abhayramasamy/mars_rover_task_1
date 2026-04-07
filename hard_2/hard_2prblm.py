import cv2
import numpy as np
import math
"""
HARD PROBLEM NO 2: Given to you a sample code that detects the dimensions of arrow using OpenCv.
The code is not complete and you have to complete the code by filling in the missing parts. 
The code should be able to detect the arrow and calculate the distance of the arrow from the camera 
using the given dimensions of the arrow and the focal length of the camera.
"""

#Added code part 1 to caluclate the focal length of the camera from given quantitoes and resolution of the camera
d = math.sqrt(1280**2 + 720**2)
f = d / (2 * math.tan(math.radians(55 / 2)))

print(f)


def detect_arrow(image_path):
    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform edge detection using Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE,
                                   cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)

        if len(approx) == 7:  # Arrows typically have 7 sides
            cv2.drawContours(image, [approx], 0, (0, 255, 0), 3)
            print("Arrow detected!")

            # Calculate bounding box
            x, y, w, h = cv2.boundingRect(approx)
            perceived_width = max(w, h)

            # Find distance (Function to be implemented)
            distance = find_distance(perceived_width)
            print(f"Estimated Distance: {distance:.2f} cm")

    # Show the result
    cv2.imshow('Detected Arrow', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

d = math.sqrt(1280**2 + 720**2)
f = d / (2 * math.tan(math.radians(55 / 2)))


#Added code part 2 to calculate the distance of the arrow from the camera 
# using the perceived width of the arrow in the image and the focal length of the camera
def find_distance(perceived_width):
    # Constants (to be calibrated)
    FOCAL_LENGTH = f  # Example focal length in pixels
    REAL_WIDTH = 17  # Real width of the arrow given
    #use law of similar triangles to calculate distance
    # Calculate distance using the formula: Distance = (Real Width * Focal Length) / Perceived Width
    distance = (REAL_WIDTH * FOCAL_LENGTH) / perceived_width
    return distance


if __name__ == "__main__":
    image_path = 'arrow_image.jpg' 
    detect_arrow(image_path)  