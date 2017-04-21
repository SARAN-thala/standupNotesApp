require 'mini_magick'


image = MiniMagick::Image.open('https://cdn-images-1.medium.com/max/1600/1*eP0V-xfRWfW3QHJhALJ5RA.jpeg')
# image = MiniMagick::Image.open('photo.jpg')

image.colorspace('gray')
image.colorspace('sRGB')


image.write('ubuntu.jpg')
