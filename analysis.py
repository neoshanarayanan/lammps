# Author: Neosha Narayanan
# UROP Summer 2019


import matplotlib.pyplot as plt


f = open("log.lammps", "r")

timesteps = []
temps = []

dataDict = {}
data_lines = []

for i, line in enumerate(f.readlines()):
    linenum = i+1
    
    if linenum >= 63 and linenum <= 89:
        data_lines.append(str.split(line))

headers = data_lines[0]
del data_lines[0]


for i, header in enumerate(headers):
    
    column = []
    for line in data_lines:
        column.append(float(line[i]))

    dataDict.update({header: column})

print(dataDict)


# dataDict shows each column stored in a list identified by header which is the key


# plot temp vs volume

temp = dataDict['KinEng']
volume = dataDict['Volume']

fig = plt.figure()
plt.plot(temp, volume)
fig.suptitle('volume vs temp', fontsize=15)
plt.xlabel('kineng', fontsize=10)
plt.ylabel('volume', fontsize=10)

fig.savefig('tempvsvolume.png')
plt.show()

f.close()
