
higharr= {'Steve': (8,1), 'Alex': (2,2), 'Wallace': (6,2), 'Andy': (5,0), 'Dan': (0,9)}
s=dict()

for entry in sorted(higharr.items(), key=lambda x: (x[1][1],-x[1][0]) ):
    print(entry)
    s[entry[0]]=entry[1]
print (s)
print('pete' in higharr)