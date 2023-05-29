

import matplotlib.image as img
import numpy as np

# reading image in variable m
m = img.imread('C:\\Users\\HP\\www\\bird.jpeg')

# Normalize the RGB values to be in the range of 0 to 1
m = m.astype(float) / 255.0

# determining dimension of image width (w) and height (h)
w, h = m.shape[:2]

# required image size after cropping
xNew = int(w * 1 / 4)
yNew = int(h * 1 / 4)
newImage = np.zeros([xNew, yNew, 4])

# print width and height of the original image
print(w)
print(h)

for i in range(xNew):
    for j in range(yNew):
        # cropping starts from 100, 100 pixels of the original image
        newImage[i, j] = m[100 + i, 100 + j]

# Save image
img.imsave('cropped.png', newImage)
