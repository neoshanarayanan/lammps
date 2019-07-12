import matplotlib.pyplot as plt


f = open("log.lammps", "r")

timesteps = []
temps = []

for i, line in enumerate(f.readlines()):
    linenum = i + 1

    if linenum >= 71 and linenum <= 122: # data is from lines 71 to 122
        split = str.split(line)
        timesteps.append(split[0])
        temps.append(split[1])


# deletes "step" and "temp" labels from arrays
del timesteps[0]
del temps[0]

print(timesteps)
print(temps)


timesteps = [float(time) for time in timesteps]
temps = [float(temp) for temp in temps]

fig = plt.figure()
plt.plot(timesteps, temps)
fig.suptitle('temperature of system over time', fontsize = 20)
plt.xlabel('time (ft)', fontsize = 14)
plt.ylabel('temp (k)', fontsize = 14)

fig.savefig('temp.png', dpi=300)
plt.show()
   

f.close()
