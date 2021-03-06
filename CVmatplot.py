from PIL import Image
from pylab import *
from numpy import *
import matplotlib.pyplot as plt

# read image to array
im = array(Image.open('data/empire.jpg'))

# plot the image
plt.imshow(im)

# some points
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

# plot the points with red star-markets
plot(x, y, 'r*')

# line plot connecting the firs two points
plot(x[:2], y[:2])

# add title and show the plot
title('Plotting: "empire.jpg"')
show()
