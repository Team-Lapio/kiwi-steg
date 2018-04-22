# -*- coding: utf-8 -*-
from PIL import Image
import random as rd

class BufferedImage:
    def __init__(self, imgPath=None):
        if imgPath is not None:
            self.__originalImage = Image.open(imgPath)
            self.__previousImage = None
            self.__currentImage = self.__originalImage.copy()
        else:
            self.__originalImage = None
            self.__previousImage = None 
            self.__currentImage = None

    def __updateImage(self, buf):
        self.__previousImage = self.__currentImage
        self.__currentImage = buf

    def __isRevertible(self):
        if self.__previousImage is not None:
            return True
        else:
            return False

    def initialize(self, image):
        self.__originalImage = Image.open(image) 
        self.__currentImage = self.__originalImage.copy()

    def getPreviousImage(self):
        buf = self.__currentImage.copy()
        if self.__isRevertible() is True:
            buf = self.__previousImage.copy()
            self.__updateImage(buf)
            return buf
        else:
            return buf

    def getCurrentImage(self):
        return self.__currentImage.copy()

    def getOriginalImage(self):
        buf = self.__originalImage.copy()
        self.__updateImage(buf)
        return buf

    def rgb_xor(self, mask=(0xFF,0xFF,0xFF)):
        '''This function performs XOR operation with given mask and currentImage field.
        Each pixel of currentImage object is XORed with given mask.
        Function returns result pillow image object through operation.
        Internally currentImage field is setted to resulting image object,
        and previousImage gets currentImage value.

        Parameter : RGB mask tuple (0~255,0~255,0~255)

        Returns : PIL Image Object
        '''
        buf = self.__currentImage.copy()
        pixelmap = buf.load()
        for i in range(buf.size[0]):
            for j in range(buf.size[1]):
                temp = pixelmap[i,j]
                pixelmap[i,j] = (temp[0] ^ mask[0], temp[1] ^ mask[1], temp[2] ^ mask[2])
        self.__updateImage(buf)
        return buf

    def rgb_and(self, mask=(0x00,0x00,0x00)):
        '''AND operation with mask and self.currentImage

        Parameter : RGB mask tuple (0~255,0~255,0~255)

        Returns : PIL Image Object
        '''
        buf = self.__currentImage.copy()
        pixelmap = buf.load()
        for i in range(buf.size[0]):
            for j in range(buf.size[1]):
                temp = pixelmap[i,j]
                pixelmap[i,j] = (temp[0] & mask[0], temp[1] & mask[1], temp[2] & mask[2])
        self.__updateImage(buf)
        return buf

    def rgb_or(self, mask=(0x00,0x00,0x00)):
        '''OR operation with mask and self.currentImage

        Parameter : RGB mask tuple (0~255,0~255,0~255)

        Returns : PIL Image Object
        '''
        buf = self.__currentImage.copy()
        pixelmap = buf.load()
        for i in range(buf.size[0]):
            for j in range(buf.size[1]):
                temp = pixelmap[i,j]
                pixelmap[i,j] = (temp[0] | mask[0], temp[1] | mask[1], temp[2] | mask[2])
        self.__updateImage(buf)
        return buf

    def randomMap(self):
        buf = self.__currentImage.copy()
        pixelmap = buf.load()
        rm, ra, rx = rd.randint(0,255), rd.randint(0,255), rd.randint(0,255)
        gm, ga, gx = rd.randint(0,255), rd.randint(0,255), rd.randint(0,255)
        bm, ba, bx = rd.randint(0,255), rd.randint(0,255), rd.randint(0,255)
        for i in range(buf.size[0]):
            for j in range(buf.size[1]):
                temp = pixelmap[i,j]
                r = (temp[0] * rm ^ rx) + ra % 255
                g = (temp[1] * gm ^ gx) + ga % 255
                b = (temp[2] * bm ^ bx) + ba % 255
                pixelmap[i,j] = (r,g,b)
        self.__updateImage(buf)
        return buf