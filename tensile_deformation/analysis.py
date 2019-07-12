# Author: Neosha Narayanan
# UROP Summer 2019


import matplotlib.pyplot as plt


f = open("log.PE_nc10_cl1000.txt", "r")

timesteps = []
temps = []

dataDict = {}
data_lines = []

for i, line in enumerate(f.readlines()):
    linenum = i+1
    
    if linenum >= 10898 and linenum <= 12617:
        data_lines.append(str.split(line))

headers = data_lines[0]
del data_lines[0]


for i, header in enumerate(headers):
    
    column = []
    for line in data_lines:
        column.append(float(line[i]))

    dataDict.update({header: column})


# dataDict shows each column stored in a list identified by header which is the key


# plot temp vs volume



param1 = "time"
param2 = "zstrain"

x = dataDict['Step']
y = dataDict['Pzz']

fig = plt.figure()
plt.plot(x, y)
fig.suptitle(param1 + ' vs '+ param2, fontsize=15)
plt.xlabel(param1, fontsize=10)
plt.ylabel(param2, fontsize=10)

fig.savefig(param2 + '_t.png')
plt.show()

f.close()
