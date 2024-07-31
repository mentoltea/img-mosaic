import PIL
from PIL import Image
import algorithm
import webbrowser
import os
import argparse
import struct
from defs import *

def main(infile, indir, strlen, minnum, maxnum):
    if indir[-1] != '/' and indir[-1] != '\\':
        indir += '/'
    image = Image.open(infile)
    
    mass: list[tuple[Image.Image, Color]] = []
    for i in range(minnum, maxnum+1):
        istr = str(i)
        filename = '0'*(strlen - len(istr)) + istr + '.png'
        img = Image.open(indir + filename)
        color = algorithm.imagecolor(img)
        mass.append((img, color))
    
    out = algorithm.alg(image, mass)
    out.save("out.png")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Args")
    parser.add_argument("infile", type=str)
    parser.add_argument("indir", type=str)
    parser.add_argument("strlen", type=int)
    parser.add_argument("minnum", type=int)
    parser.add_argument("maxnum", type=int)
    
    args = parser.parse_args()
    main(args.infile, args.indir, args.strlen, args.minnum, args.maxnum)