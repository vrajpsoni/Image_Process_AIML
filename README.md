# Enhancing Images with OpenCV

This OpenCV-compatible image improvement module applies different filters to improve the quality of images. It works especially well with grayscale photos. It uses gamma correction to keep the image from being too dark, histogram equalization to boost contrast, and a median filter to remove noise.

## Getting started

Prerequisites for running the code are:

Python =3.5<br/>
python-opencv =4.2.0<br/>
scipy =1.3.1<br/>

or

```
pip install opencv-python
```
```
pip install scipy
```

## Features

- Utilize the median_filter to remove noise from a grayscale image.
- Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) for histogram equalization of the image.
- Enhance sharpness and contrast of the images.
- Employ gamma correction to prevent darkening of the images. 

## Usage

Inside the project's directory run:

```
python image_enhancement.py
```
You can find sample images in the Dataset folder and results can be generated in Results folder.

These code works better for gray scale images.

### Results
### Original Image
<img src="images/image1.jpg" width = "300" height = "225"/> <img src="images/image2.jpg" width = "300" height = "225"/>

### Processed Image
<img src="images/result1.jpg" width = "300" height = "225"/> <img src="images/result2.jpg" width = "300" height = "225"/>



------

## Keywords

#vrajsoni #vrajsoni.com # umass #umassbeacon #beacon #umassboston #