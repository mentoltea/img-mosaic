# IMAGE MOSAIC
# HOW TO USE
There are presented 2 exe-files: start.exe and edit.exe

To make a mosaic you use start.exe

To edit the size of images you use edit.exe

# START.EXE
To make a mosaic you use start.exe providing parameters in this order:
* infile - Name of input file (single)
* indir - Directory with images used for mosaic. The images should be named only with numbers in order. For example, 0001.png, 0002.png, ..., 9201.png
* strlen - The length of the name of images (excluding the format). For example, 0001.png has the length of 4. Should be the same for all images in indir
* minnum - The number images start with
* maxnum - The number images end with

Example of usage:
start.exe .\in.png .\rickroll_minimum\ 5 1 212

# EDIT.EXE
To edit the size of images you use edit.exe providing parameters in this order:
* indir - Directory with images used for mosaic. The images should be named only with numbers in order. For example, 0001.png, 0002.png, ..., 9201.png
* outdir - Directory to output edited images
* strlen - The length of the name of images (excluding the format). For example, 0001.png has the length of 4. Should be the same for all images in indir
* minnum - The number images start with
* maxnum - The number images end with
* sizex - The x-value size of edited images
* sizey - The y-value size of edited images

Example of usage:
edit.exe .\rickroll_minimum\ .\rickroll_minmin\ 5 1 212 10 8

# PURPOSE
The only purpose and goal for this programm was to make instant-rickroll images, but maybe you will find more practical usage for it