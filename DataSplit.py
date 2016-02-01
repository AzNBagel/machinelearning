import numpy as np

fileData = np.loadtxt('newtraining.txt', delimiter = ',')


def writeOut(filename, dataOut):
    with open(filename, 'w') as f:
        f.write(dataOut)

print fileData.shape
filesOut = []
for i in range(26):
    temp = fileData[fileData[:,0] == float(i)]
    filesOut.append(temp)
    #writeOut(unichr(i+65),temp)


print filesOut[0]





