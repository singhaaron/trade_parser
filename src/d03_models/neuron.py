import math
import numpy as np

class Neuron:
	def __init__(self):
		pass
	def fit(self,X,y,epochs,loss_threshold):
		pass
	def batch_gradient_descent(self,input_vector,y_true,epochs,loss_threshold):
		'''
		type: optimization function
		objective: reach global minima 
		'''
		pass
	# activation function
	def sigmoid(x):
		return 1/(1+math.exp(-x))
	def sigmoid_numpy(x):
		return 1/(1+np.exp(-x))
	def log_loss(y_true,y_predicted):
		'''
		type: 
		summary: measures how close the prediction is to corresponding actual | true value
		higher evergence indicates higher log loss
		'''
		epilson = 1e-15
		y_predicted_new = [max(_,epilson) for _ in y_predicted]
		y_predicted_new = [min(_,epilson) for _ in y_predicted]
		y_predicted_new = np.array(y_predicted)
		return -np.mean(y_true*np.log(y_predicted_new)+(1-y_true)*np.log(1-y_predicted_new))
