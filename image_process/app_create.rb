require 'mini_magick'

image = MiniMagick::Image.open('https://cdn-images-1.medium.com/max/1600/1*eP0V-xfRWfW3QHJhALJ5RA.jpeg')
# image = MiniMagick::Image.open('Mac.jpeg')
#
#image.resize "300x10000"

image.colorspace 'gray'

# image.format 'JPEG'

image.write('macOS.jpeg')

#
# image.format 'png'
# image.colorspace('gray')
# image.fill('rgb(68,48,228)')
# image.tint(100)
# image.brightness_contrast("20x0")
#
# image.write('output2.png')