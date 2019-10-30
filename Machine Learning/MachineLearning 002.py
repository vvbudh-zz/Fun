#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday Oct 2, 2018
@author: Madhuri Suthar, PhD Candidate in Electrical and Computer Engineering, UCLA
"""

# Imports
import numpy as np

# Each row is a training example, each column is a feature  [X1, X2, X3]
X = np.array(([0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]), dtype=float)
y = np.array(([0], [1], [1], [0]), dtype=float)


# Define useful functions

# Activation function
def sigmoid(t):
    return 1 / (1 + np.exp(-t))


# Derivative of sigmoid
def sigmoid_derivative(p):
    return p * (1 - p)


# Class definition
class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1], 4)  # considering we have 4 nodes in the hidden layer
        self.weights2 = np.random.rand(1, 4)
        self.y = y
        self.output = np.zeros(y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.layer2 = sigmoid(np.dot(self.layer1, self.weights2))
        return self.layer2
#back propogation, corrects the errors.
    def backprop(self):
        d_weights2 = np.dot(self.layer1.T, 2 * (self.y - self.output) * sigmoid_derivative(self.output))
        d_weights1 = np.dot(self.input.T, np.dot(2 * (self.y - self.output) * sigmoid_derivative(self.output),
                                                 self.weights2.T) * sigmoid_derivative(self.layer1))

        self.weights1 += d_weights1
        self.weights2 += d_weights2
#the definition to train the Neural Network.
    def train(self, X, y):
        self.output = self.feedforward()
        self.backprop()


NN = NeuralNetwork(X, y)
for i in range(1500):  # trains the NN 1,000 times. looks like 1500 times.
    if i % 100 == 0:
        print("for iteration # " + str(i) + "\n")
        print("Input : \n" + str(X))
        print("Actual Output: \n" + str(y))
        print("Predicted Output: \n" + str(NN.feedforward()))
        print("Loss: \n" + str(np.mean(np.square(y - NN.feedforward()))))  # mean sum squared loss
        print("\n")

    NN.train(X, y)
'''
NN2 = NeuralNetwork(X, y)
for i in range(10):  # trains the NN 1,000 times. looks like 1500 times.
    #if i % 100 == 0:
    if i > 0:
        print("for iteration # " + str(i) + "\n")
        print("Input : \n" + str(X))
        print("Actual Output: \n" + str(y))
        print("Predicted Output: \n" + str(NN2.feedforward()))
        print("Loss: \n" + str(np.mean(np.square(y - NN2.feedforward()))))  # mean sum squared loss
        print("\n")

        NN2.train(X, y)
'''