import os
from PIL import Image as pil

size = 128, 128
infilename = 'c:\photos\sky\8\DSC05827.jpg '
im = pil.open(infilename)
i2=im.crop([0,0,100,100])
i2.show()

#im.thumbnail(size, pil.ANTIALIAS)
pix=im.load()


for i in range(0 ,127):
    for j in range(0, 127):
        print (i,j ,pix[i,j])

# mirror = myimage.transpose(pil.ROTATE_90)
#mirror.show()
#outfilename = "c:\\photos\\sky\\8\\"+os.path.splitext(os.path.basename(infilename))[0] + "_r90.png"
#mirror.save(outfilename)