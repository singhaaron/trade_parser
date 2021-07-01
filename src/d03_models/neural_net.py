import sys
import numpy as np
import matplotlib

print("Python", sys.version)
print("Numpy", np.__version__)
print("Matplotlib", matplotlib.__version__)


# inputs = [1, 2, 3]
# weights = [0.2, 0.8, -0.5]
# bias = 2
# output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias
# print(output)

# inputs = [1, 2, 3, 2.5]
# weights = [0.2, 0.8, -0.5, 1.0]
# bias = 2
# output = (
#     inputs[0] * weights[0]
#     + inputs[1] * weights[1]
#     + inputs[2] * weights[2]
#     + inputs[3] * weights[3]
#     + bias
# )
# print(output)

# inputs = [1, 2, 3, 2.5]
# weights1 = [0.2, 0.8, -0.5, 1.0]
# weights2 = [0.5, -0.91, 0.26, -0.5]
# weights3 = [-0.26, -0.27, 0.17, 0.87]
# bias1 = 2
# bias2 = 3
# bias3 = 0.5
# output = [
#     inputs[0] * weights1[0]
#     + inputs[1] * weights1[1]
#     + inputs[2] * weights1[2]
#     + inputs[3] * weights1[3]
#     + bias1,
#     inputs[0] * weights2[0]
#     + inputs[1] * weights2[1]
#     + inputs[2] * weights2[2]
#     + inputs[3] * weights2[3]
#     + bias2,
#     inputs[0] * weights3[0]
#     + inputs[1] * weights3[1]
#     + inputs[2] * weights3[2]
#     + inputs[3] * weights3[3]
#     + bias3,
# ]
# print(output)


# weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
# inputs = [1, 2, 3, 2.5]
# biases = [2, 3, 0.5]
# layer_outputs = []
# for neuron_weights, neuron_bias in zip(weights, biases):
#     print("_")
#     # print("Neuron Weight: {} & Neuron Bias: {}".format(neuron_weights, neuron_biases))
#     neuron_output = 0
#     for n_input, weight in zip(inputs, neuron_weights):
#         neuron_output += n_input * weight
#     neuron_output += neuron_bias
#     layer_outputs.append(neuron_output)
#     # print("Input: & {} Weight:{}".format(n_input, weight))
# print(layer_outputs)

# inputs = [1, 2, 3, 2.5]
# weights = [0.2, 0.8, -0.5, 1.0]
# bias = 2

# output = np.dot(weights, inputs) + bias
# print(output)

# weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
# inputs = [1, 2, 3, 2.5]
# biases = [2, 3, 0.5]

# output = np.dot(weights, inputs) + biases
# print(output)

# # Batching Samples Doesn't work w/Products because of size
# weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
# inputs = [[1, 2, 3, 2.5], [2.0, 5.0, -1.0, 2.0], [-1.5, 2.7, 3.3, -0.8]]
# biases = [2, 3, 0.5]

# output = np.dot(weights, inputs) + biases
# print(output)


# # Batch Size:
# learning rate: moving forward, how much do you want to keep the previous knowledge
# figment line

# weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
# inputs = [[1, 2, 3, 2.5], [2.0, 5.0, -1.0, 2.0], [-1.5, 2.7, 3.3, -0.8]]
# biases = [2, 3, 0.5]

# output = np.dot(inputs, np.array(weights).T) + biases
# print(output)


# Multipler layers
# weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
# weights2 = [[0.1, -0.14, 0.5], [-0.5, 0.12, -0.33], [-0.44, 0.73, -0.13]]
# inputs = [[1, 2, 3, 2.5], [2.0, 5.0, -1.0, 2.0], [-1.5, 2.7, 3.3, -0.8]]
# biases = [2, 3, 0.5]
# biases2 = [-1, 2, -0.5]

# layer1_output = np.dot(inputs, np.array(weights).T) + biases
# layer2_output = np.dot(layer1_output, np.array(weights2).T) + biases2

# print(layer2_output)
# X: Input Data to Neural Network
X = [[1, 2, 3, 2.5], [2.0, 5.0, -1.0, 2.0], [-1.5, 2.7, 3.3, -0.8]]

np.random.seed(0)
# Hidden Layer Implementation
class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        # size of the input : n_inputs
        self.weights = np.random.randn(n_inputs, n_neurons)  # paramater as shape
        self.biases = np.zeros((1, n_neurons))  # passing parameter as shape
        pass

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights)
        pass


print(0.10 * np.random.randn(4, 3))
layer1 = Layer_Dense(4, 5)
layer2 = Layer_Dense(5, 2)
layer1.forward(X)
layer2.forward(layer1.output)
print(layer1.output)
