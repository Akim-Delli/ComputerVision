from PIL import Image
from pylab import *
from numpy import *
import matplotlib.pyplot as plt

# read image to array
im = array(Image.open('data/empire.jpg'))

# plot the image
plt.imshow(im)

print 'Please click 3 points'
x = ginput(3)
print 'you clicked:', x
show()
