import os
import re
import operator
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
print(starlist)
starlist.sort(key=operator.itemgetter(1),reverse=True)
print(starlist)
fw = open(outfilename, 'w')
nstars=1
for s in starlist:
    print(s[2][0],s[2][1])
    if float(s[1]) >0.6:
        fw.write(s[2][0]+s[2][1]+'\n')
        nstars+=1
print (nstars)