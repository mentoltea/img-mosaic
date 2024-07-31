import PIL
from PIL import Image
import math
import random
from defs import *


def getcolor(img: Image.Image, px: int, py: int) -> Color:
    col: tuple[int, int, int] = img.getpixel((px, py))
    return Color(col)

def format(img: Image.Image, xsize: int, ysize:int) -> Image.Image:
    return img.resize((xsize, ysize))

def imagecolor(img:Image.Image) -> Color:
    (xsize, ysize) = img.size
    color = Color((0,0,0))
    for x in range(xsize):
        for y in range(ysize):
            color += getcolor(img, x, y)
    color = color / (xsize*ysize)
    return color

def alg(image: Image.Image, construct: list[tuple[Image.Image, Color]]) -> Image.Image:
    image = image.convert("RGB")
    
    (blockx, blocky) = construct[0][0].size
    (xsize, ysize) = image.size
    
    const = construct.copy()
    
    img = Image.new(mode="RGB", size=(xsize, ysize))
    numx = int(xsize/blockx)
    numy = int(ysize/blocky)
    if (blockx*numx < xsize):
        numx += 1
    if (blocky*numy < ysize):
        numy += 1
    
    for bx in range(numx):
        for by in range(numy):
            # Block (bx, by)
            color = Color((0,0,0))
            for x in range(bx*blockx, min((bx+1)*blockx, xsize)):
                for y in range(by*blocky, min((by+1)*blocky, ysize)):
                    color += getcolor(image, x, y)
            
            if len(const)==0:
                const = construct.copy()
            color: Color = color/(blockx*blocky)
            
            const.sort(key= lambda t: color.distsq(t[1]))
            (resimg, rescol) = const[0]
            const.pop(0)
            img.paste(resimg, (bx*blockx, by*blocky))
    
    return img