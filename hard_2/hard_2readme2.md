# Arrow Detection and Distance Estimation using OpenCV

## Problem Title

Arrow Detection and Distance Estimation using Pinhole Camera Model

---

## Problem Overview

This task involves detecting an arrow in an image using computer vision techniques and estimating its distance from the camera. The system processes an input image, identifies arrow-like contours, and computes the distance based on the perceived size of the object.

---

## Inputs

1. Image Input
   An image/frame captured from a webcam.

2. Camera Specifications

* Resolution: 1280 × 720 pixels
* Diagonal Field of View (FOV): 55 degrees

3. Real Object Dimension

* Actual width of arrow: 17.0 cm

---

## Outputs

* Detection of arrow in the image
* Bounding contour drawn around the arrow
* Estimated distance of the arrow from the camera (in cm)

---

## Methods Used (opencv and distance_estimation)

**Note, some parts of the following approach are already included in the partially complete file**

1. Image Preprocessing

* Convert image to grayscale
* Apply Gaussian Blur to reduce noise

2. Edge Detection

* Use Canny Edge Detection to extract edges

3. Contour Detection

* Extract contours from edge map
* Approximate contours using polygon approximation

4. Shape Filtering

* Identify arrow based on number of polygon vertices (approx = 7 sides)

5. Bounding Box Extraction

* Compute bounding rectangle around detected arrow
* Use maximum of width/height as perceived width

6. Distance Estimation

* Apply pinhole camera model to estimate distance

---
## Law of Similar Triangles

The pinhole camera model is based on the principle of similar triangles. When an object is viewed through a camera, the real-world object and its projection on the image plane form two similar triangles.

This relationship allows us to relate real-world dimensions with image dimensions.

Let:

* ( W ) = real width of the object
* ( D ) = distance from camera to object
* ( w ) = perceived width in the image (in pixels)
* ( f ) = focal length of the camera (in pixels)

Using similarity of triangles:

$
\frac{W}{D} = \frac{w}{f}
$

Rearranging to compute distance:

$
D = \frac{f \cdot W}{w}
$

This equation forms the basis for distance estimation in the implemented system.
--

## Key Equations

1. Diagonal Pixel Length

```
d = sqrt(width^2 + height^2)
```

2. Focal Length Calculation

```
f = d / (2 * tan(FOV / 2))
```

3. Distance Estimation

```
Distance = (f × Real Width) / Perceived Width
```

---

## Approach

1. Load image using OpenCV.
2. Convert to grayscale and apply Gaussian blur.
3. Perform Canny edge detection.
4. Extract contours from the edge image.
5. Approximate each contour to a polygon.
6. Filter contours with approximately 7 vertices (arrow-like shape).
7. Draw contour and compute bounding box.
8. Measure perceived width in pixels.
9. Compute focal length using FOV and resolution.
10. Estimate distance using pinhole camera equation.
11. Display results on the image.

---

## Learning Experience

* Practical understanding of image processing pipeline
* Implementation of contour-based shape detection
* Application of pinhole camera model in real scenarios
* Importance of preprocessing in computer vision tasks
* Trade-offs between accuracy and computational simplicity

---

## Resources Used

* Basic references on pinhole camera model
* Trigonometry for focal length calculation

---

## Conclusion

The system successfully detects arrow shapes in an image and estimates their distance using geometric principles.
