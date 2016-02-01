

"""
Andrew McCann
Machine Learning 445
Winter 2016
Utility to split data sets
Specifically for Homework 1
"""
"""
splitLen = 20         # 20 lines per file
#outputBase = 'output' # output.1.txt, output.2.txt, etc.

input = open('data.txt', 'r').read().split('\n')

at = 1
for lines in range(0, len(input), splitLen):
    # First, get the list slice
    outputData = input[lines:lines+splitLen]

    # Now open the output file, join the new slice with newlines
    # and write it out. Then close the file.
    output = open(outputBase + str(at) + '.txt', 'w')
    output.write('\n'.join(outputData))
    output.close()

    # Increment the counter
    at += 1

#My version to cut the file in half

inData = open('letter-recognition.data', 'r').read().split('\n')

halfPoint = len(input)/2
outTrain = open('training.txt', 'w')
outTest = open('test.txt', 'w')

for lines in range(0, len(input),halfPoint):
    outData = input[lines:lines+halfPoint]
    outTrain.write('\n'.join(outData))


outFile.close()


outFile = open('test.txt','w')



outData = input[lines:halfPoint + len(input)]
outFile.write(outData)
outFile.close()


# Starting point for splitting file into individual letters.
# Who knows what spice


"""

def shuffle_split(infilename, outfilename1, outfilename2):
    from random import shuffle

    with open(infilename, 'r') as f:
        lines = f.readlines()

    # append a newline in case the last line didn't end with one
    lines[-1] = lines[-1].rstrip('\n') + '\n'

    shuffle(lines)

    with open(outfilename1, 'w') as f:
        f.writelines(lines[:len(lines) // 2])
    with open(outfilename2, 'w') as f:
        f.writelines(lines[len(lines) // 2:])


shuffle_split('letter-recognition.data', 'training.txt', 'test.txt')













