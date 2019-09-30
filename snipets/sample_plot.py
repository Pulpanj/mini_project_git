import os
import re
import operator
import numpy as np
import matplotlib.pyplot as plt
# plt.clf
# plt.figure()          # Make a new figure window
# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()
import numpy as np
from PIL import Image
image = Image.open('c:/photos/sky/16/out/Autosave002small.jpg ')
xsize, ysize = image.size
print("Image size: {} x {}".format(xsize, ysize))

plt.figure( 1,figsize=[15,10])
plt.imshow(image)
infilename = 'c:\\ajps\\sky\\DSC06411.Info.txt'
outfilename = 'c:\\ajps\\sky\\DSC06411.stars2.txt'
fp = open(infilename, 'r')
line = fp.readline()
cnt = 1
starlist=[]
star=[]
while line:
    if line.split('=')[0] =='Star# ':
        if cnt >6:
            starno=re.split('[,=\n]',line)
    if line.split('=')[0] == 'Intensity ':
        Intensity = re.split('[,=\n]', line)
    if line.split('=')[0] == 'Center ':
        center = re.split('[,=\n]', line)
        star=[starno[1],Intensity[1],center[1:3]]
        starlist.append(star)
    line = fp.readline()
    cnt += 1
# print(starlist)
starlist.sort(key=operator.itemgetter(1),reverse=True)
nstars=1  # type: int
x=[]
y=[]
fmt=[]
for s in starlist:
    if float(s[1]) >0.4:
        x.append(float(s[2][0])*xsize/5472)
        y.append(float(s[2][1]) *ysize/3648)
        fmt.append(s[1])
        nstars+=1
print (fmt)
font_dict = {'family': 'serif',
             'color': 'white',
             'size': 15}
for i in range(0,len(x)):
    if float(starlist[i][1]) >0.6:
        plt.text(text=fmt[i], x=x[i],y=y[i],s='none',fontdict=font_dict)
plt.plot(x, y, 'D', fillstyle='none',markersize=10)
plt.show()