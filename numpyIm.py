from PIL import Image
from numpy import *
import imtools

# read image to array
im = array(Image.open('data/empire.jpg'))
print im.shape, im.dtype

im = array(Image.open('data/empire.jpg').convert('L'), 'f')
print im.shape, im.dtype

im = array(Image.open('data/empire.jpg').convert('L'))

# invert image
im2 = 255 - im

# clamp to interval 100...200
im3 = (100.0/255) * im + 100

# squared
im4 = 255.0 * (im/255.0)**2

print int(im4.min()),  int(im4.max())

# ====================================
im = array(Image.open('data/AquaTermi_lowcontrast.JPG').convert('L'))
im5, cdf = imtools.histeq(im)





