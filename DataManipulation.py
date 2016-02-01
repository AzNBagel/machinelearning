import fileinput
import re
import numpy as np

fileData = np.genfromtxt('training.txt', delimiter=',', dtype='O')

for i in range(len(fileData)):
    fileData[i,0] = ord(fileData[i,0]) - 65.
fileData = fileData.astype(np.float32)

filesOut = []
for i in range(26):
    temp = fileData[fileData[:,0] == float(i)]
    filesOut.append(temp)



print(fileData.shape)
print(filesOut[3])
print(fileData[:5,0])
#np.savet('newtraining.txt', fileData)
#fileData.tofile('trial.txt', format=str)

