from PIL import Image
from pylab import *
from numpy import *
import matplotlib.pyplot as plt

# read image to array
im = array(Image.open('data/empire.jpg').convert('L'))

# create a new figure
figure()

# don't use colors
gray()
# show contours with origin upper left corner
contour(im, origin='image')
axis('equal')
axis('off')

figure()
hist(im.flatten(), 128)
show()