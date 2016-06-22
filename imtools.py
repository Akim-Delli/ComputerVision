import os
from PIL import Image
from numpy import *


def get_imlist(path):
    """Returns a list of filenames for
    all jpg images in a directory"""

    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]


def imresize(im, sz):
    """ Resize an image array using PIL. """
    pil_im = Image.fromarray(uint8(im))

    return array(pil_im.resize(sz))


def histeq(im, nbr_bins=256):
    """ Histogram equalization of a grayscale image """
    # get image histogram
    im_hist, bins = histogram(im.flatten(), nbr_bins, normed=True)
    # cumulative distribution function
    cdf = im_hist.cumsum()
    # normalize
    cdf = 255 * cdf / cdf[-1]

    # use linear interpolation of cdf to find new pixel values
    im2 = interp(im.flatten(), bins[:-1], cdf)

    return im2.reshape(im.shape), cdf


def compute_average(im_list):
    """ Compute the average of a list of images """

    # open first image and make into array of type float
    average_im = array(Image.open(im_list[0], 'f'))

    for im_name in im_list[1:]:
        try:
            average_im += array(Image, open(im_name))
        except:
            print im_name + '...skipped'
    average_im /= len(im_list)

    # return average as uint8
    return array(average_im, 'uint8')
