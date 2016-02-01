import numpy as np
import math
import random



perceptronList = []

weights = []

        # Initialize random weights for this Individual perceptron including bias
for i in range(16): # 16 inputs plus a 17th for bias
    weights.append(random.uniform(-1,1))

print(weights)