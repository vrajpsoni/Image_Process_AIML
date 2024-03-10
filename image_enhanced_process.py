#--------------------------------
# Date : 10 March 2024
# Project : Image Enhancement with Python AIML
#--------------------------------
import os
import cv2
from scipy import ndimage
from datetime import datetime

SOURCE_PATH = 'storage/source/'
DESTINATION_LOCATION = 'storage/destination/'

def enhanceImage(path):
    for filename in os.listdir(path):
        try:
            image = cv2.imread(path + filename)

            if image is not None:
                # Convert image to gray scale
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                # Apply a non-linear filter to remove noise
                deNoised = ndimage.median_filter(gray_image, 3)

                # Apply Histogram Equalization
                # Enhance contrast using a high-pass filter
                clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
                highPass = clahe.apply(deNoised)

                # Apply Gamma Transformation
                # Prevent bleaching or darkening of images
                gamma = highPass / 255.0
                gammaFilter = cv2.pow(gamma, 1.5)
                gammaFilter = gammaFilter * 255

                # Generate timestamp
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

                # Append timestamp to filename

                output_filename = os.path.splitext(filename)[0] + '_' + timestamp + os.path.splitext(filename)[1]

                cv2.imwrite(DESTINATION_LOCATION + output_filename, gammaFilter)
        except:
            print('Image not found')

print("---------------------------------------------")
print("***** Initializing *****")
# Output enhanced images
enhanceImage(path=SOURCE_PATH)
print("***** Processed file location:" + " (" + DESTINATION_LOCATION + ") " "*****")
print("***** Process Completed *****")
print("---------------------------------------------")
