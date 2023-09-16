# -*- coding: utf-8 -*-
"""Image processing with pillow in Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16NubQrVhJ0YBywd-ykczZ6E950aXDiLM
"""

pip install pillow

from PIL import Image as Myimage
import PIL.ImageDraw as MyimageDraw
import PIL.ImageFont as Myimagefont

import matplotlib.pyplot as plt

import PIL.Image as Myimg
import PIL.ImageFilter as Myfilter

from google.colab import files

uploaded = files.upload()

image = Myimage.open("me_2021.jpg")

plt.imshow(image)

#Save image with different Formate!,BMP, PNG , JPEG , TIFF

image.save("me_2021.png") #use ext in the end!

#Customize Qualitlies
image.save("me_2021.jpeg" , qualities = 90)

#Image attributes formate , size , color
image = Myimage.open("me_2021.jpg")
print("Type :",type(image))
print("Size :" , image.size)
print("Formate :" , image.format)
print("Color Mode :",image.mode)

#Resize Image

image = Myimage.open("me_2021.jpg")
resize = image.resize((200,200))
plt.imshow(resize)

#Rotate Image
image = Myimage.open("me_2021.jpg")
rotate = image.rotate(30)
plt.imshow(rotate)
rotate.save("you_2021.png") # we can save also in different format

#Create a Thumbnail Image
#image = Myimage.open("me_2021.jpg")
#image_Copy = image.copy()
#final = image_Copy.thumbnail((100, 100))
#plt.imshow(final)

#crop Image
image = Myimage.open("me_2021.jpg")
cropimg = image.crop((150, 80 , 300 , 300))
plt.imshow(cropimg)

#Rotate and flip images (transpose)
image = Myimage.open("me_2021.jpg")
transpos_img = image.transpose(Myimage.ROTATE_270) #rotate, 90, 180 etc
flip_img = image.transpose(Myimage.FLIP_LEFT_RIGHT) #or FLIP.TOP_BOTTOM
plt.imshow(transpos_img)
plt.imshow(flip_img)

#Filters
image = Myimage.open("me_2021.jpg")
#blur_image = image.filter(Myfilter.BLUR)
#blur_image = image.filter(Myfilter.BoxBlur(3))
blur_image = image.filter(Myfilter.GaussianBlur(radius = 10))
plt.imshow(blur_image)

#Contous Filter
image = Myimage.open("me_2021.jpg")
blur_image = image.filter(Myfilter.CONTOUR)
plt.imshow(blur_image)

#Detailed filter!
image = Myimage.open("me_2021.jpg")
detail_image = image.filter(Myfilter.DETAIL)
plt.imshow(detail_image)

#Edge enhance filter!
image = Myimage.open("me_2021.jpg")
edge_enhance = image.filter(Myfilter.EDGE_ENHANCE)
plt.imshow(edge_enhance)

#EMBOS FILTER!

image = Myimage.open("me_2021.jpg")
embos_image = image.filter(Myfilter.EMBOSS)
plt.imshow(embos_image)

#Find Edge Filter!

image = Myimage.open("me_2021.jpg")
find_edge = image.filter(Myfilter.FIND_EDGES)
plt.imshow(find_edge)

#ADDING SMOOTH AND SMOOTH MORE FILTER

image = Myimage.open("me_2021.jpg")
Smooth_filter = image.filter(Myfilter.SMOOTH) #Myfilter.SMOOTHMORE
plt.imshow(Smooth_filter)

#Adding Sharpen filter
image = Myimage.open("me_2021.jpg")
Sharpen_filter = image.filter(Myfilter.SHARPEN)
plt.imshow(Sharpen_filter)

"""**Add Simple text to Image as Watermark**"""

image = Myimage.open("me_2021.jpg")
Watermark = MyimageDraw.Draw(image)
Watermark.text((28, 30) , "Hello Pyhton!" , fill =(225 , 0 ,0)) #red , green, blue
plt.imshow(image)

"""**Add text (Watermark) with custom font to image**"""

image = Myimage.open("me_2021.jpg")
#Myfot = Myimagefont.truetype("Font/tahoma.ttf" , 20) #otf ttf
Watermark = MyimageDraw.Draw(image)
Watermark.text((28, 30) , "Hello Pyhton!" , fill =(225 , 0 ,0)) #red , green, blue
plt.imshow(image)

"""**Split image bands ( Color Channels)**"""

image = Myimage.open("me_2021.jpg")
ColorBands = image.split()
r:Myimage.image = ColorBands[0] #0 ,1, 2
#im: Myimage.merge("RGB" , (r,g ,b))
plt.imshow(r)