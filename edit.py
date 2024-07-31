import PIL
from PIL import Image
import algorithm
import webbrowser
import os
import argparse
import struct

def main(indir, outdir, strlen, minnum, maxnum, sizex, sizey):
    if indir[-1] != '/' and indir[-1] != '\\':
        indir += '/'
    if outdir[-1] != '/' and outdir[-1] != '\\':
        outdir += '/'
    
    for i in range(minnum, maxnum+1):
        istr = str(i)
        filename = '0'*(strlen - len(istr)) + istr + '.png'
        img = Image.open(indir + filename)
        # (xs, ys) = img.size
        # img = img.crop((178, 0, xs-178, ys))
        img = img.resize((sizex, sizey))
        img.save(outdir + filename)
        
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Args")
    parser.add_argument("indir", type=str)
    parser.add_argument("outdir", type=str)
    parser.add_argument("strlen", type=int)
    parser.add_argument("minnum", type=int)
    parser.add_argument("maxnum", type=int)
    parser.add_argument("sizex", type=int)
    parser.add_argument("sizey", type=int)
    
    args = parser.parse_args()
    main(args.indir, args.outdir, args.strlen, args.minnum, args.maxnum, args.sizex, args.sizey)