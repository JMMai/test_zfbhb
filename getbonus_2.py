#!/usr/bin/env python
# created by yao
# 2016.12.23
from PIL import Image
im = Image.open('E:/PythonDev/支付宝红包/Screenshot_20161226-142407.png')

imgWidth = 420 # width of the image you cut off
startX = 330
startY = 974 # the first line position-y
splitPoxis = 8 # split height
blackHeigh = 8 # black line height
s1 = 8
b1 = 6
s2 = 6
b2 = 10

maxLineNumber = 27
hMN = 30


# function to deal image
def pasteImg( startY, index):
    #print("inside index:", index)
    #第一次从上边沿取色覆盖
    box = (startX, startY + splitPoxis*index-blackHeigh//2,startX + imgWidth,startY + splitPoxis*index)
    #print box
    region = im.crop(box)
    
    box_dealed = (startX,startY + splitPoxis * index,startX + imgWidth,startY + splitPoxis*index + blackHeigh//2)
    #print box
    #region_dealed = im.crop(box_dealed)
    
    im.paste( region, box_dealed )

    #第二次从下边沿取色块覆盖
    box = (startX, startY + splitPoxis*index + blackHeigh, startX + imgWidth, startY + splitPoxis * index + blackHeigh*3//2)
    #print box
    region = im.crop(box)
    
    box_dealed = (startX,startY + splitPoxis * index + blackHeigh//2, startX + imgWidth, startY + splitPoxis*index + blackHeigh)
    #print box
    #region_dealed = im.crop(box_dealed)
    
    im.paste( region, box_dealed )



pasteImg(startY, 0)

#for index in range(1,maxLineNumber):
for index in range(1,hMN):
    #print("outside index:", index)
    pasteImg( startY, index )


im.save('IMG_0257.dealed.jpg')
im.show()
