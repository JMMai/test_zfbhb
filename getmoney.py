#!/usr/bin/env python
# created by yao
# 2016.12.23
# Enhanced by Mai on 2016.12.27
# 新版本使用黑线坐标文件暴力去黑线，分两次取正常图片区域去覆盖一条黑线，尽量使图片平滑些
# 程序使用华为Mate 9的截图测试通过，黑线坐标估计和手机屏幕分辨率有关，
# 如果你的手机屏幕分辨率不是1080×1920，去黑线效果有可能不同，请针对你的手机截图修改黑线坐标文件
from PIL import Image


#Blackline position file
blackLinePosFile = 'E:/PythonDev/支付宝红包/blpos.txt'

#Image file folder and file name
sourceFileFolder = "E:/PythonDev/支付宝红包/"
sourceFileName = "Screenshot_20161230-174521.png"
sfn, sfe = sourceFileName.split(".")

im = Image.open(sourceFileFolder + sourceFileName)

imgWidth = 420 # width of the image you cut off
startX = 330
startY = 973 # the first line position-y

# function to deal image
def pasteImg( bStartPos, bEndPos):
    bsp = int(bStartPos)
    bep = int(bEndPos)
    blackLineHeight = bep - bsp
    if blackLineHeight%2 != 0:        #黑线高度是奇数
        blackLineHeight = blackLineHeight + 1  
        hbh_u = blackLineHeight//2
        hbh_b = (blackLineHeight - 2)//2
    else:
        hbh_u = blackLineHeight//2
        hbh_b = hbh_u

    #为了使图片尽量平滑，一条黑线分两次覆盖
    #第一次从黑线上边沿取色覆盖
    box = (startX, bsp - hbh_u, startX + imgWidth, bsp)
    #print box
    region = im.crop(box)
    
    box_dealed = (startX, bsp, startX + imgWidth, bsp + hbh_u)
    #print box
    #region_dealed = im.crop(box_dealed)
    
    im.paste( region, box_dealed )

    #第二次从黑线下边沿取色块覆盖
    box = (startX, bep, startX + imgWidth, bep + hbh_b)
    #print box
    region = im.crop(box)
    
    box_dealed = (startX, bsp + hbh_u, startX + imgWidth, bsp +hbh_u + hbh_b)
    #print box
    #region_dealed = im.crop(box_dealed)
    
    im.paste( region, box_dealed )



#读黑线开始位置和结束位置
with open(blackLinePosFile,'r',encoding='utf-8') as pf:

    for y in pf:
         #取字符串第一个字符看是否是数字，如果不是，跳过注释和标题
        if not(y[0:1].isdigit()):
            continue
        
        bPos, ePos = y.strip().split("\t")
        pasteImg( bPos, ePos )



im.save(sfn + ".dealed." + sfe)
im.show()
#接下来就是扫红包的时刻，祝你好运！
