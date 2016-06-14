from PIL import Image

# convert an image to thumbnail
pil_im = Image.open('data/empire.jpg')
pil_im.thumbnail((128, 128))
pil_im.save('data/output/empire-thumbnail.jpg')

# Cropping a region of an image
pil_img2 = Image.open('data/empire.jpg')
box = (100, 100, 400, 400)
region = pil_img2.crop(box)
region = region.transpose(Image.ROTATE_180)
pil_img2.paste(region, box)
pil_img2.save('data/output/empire-cropped.jpg')

# Resize
pil_im3 = Image.open('data/empire.jpg')
out = pil_im3.resize((128, 128))
out.save('data/output/empire-resize.jpg')

# Rotate
out = pil_im3.rotate(45)
out.save('data/output/empire-rotate.jpg')


