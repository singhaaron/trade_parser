import math

def sigmoid(x):
    return 1/(1+math.exp(-x))

print(sigmoid(1000))
print(sigmoid(-56))