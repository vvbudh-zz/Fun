import numpy as np



class NeuralNetwork():
    def __init__(self):
        np.random.seed(1)

        self.synapticWeights = 2 * np.random.random((3,1)) -1

    def sigmoid(self, x):
        print("Running the sigmoid now.")
        return 1/ (1 + np.exp(-x))

    def sigmoidDerivative(self, x):
        print("Running the derivative of the sigmoid now.")
        return x * (1 - x)

    def train(self, trainingInputs, trainingOutputs, trainingIterations):
        print("This is the train function")
        for iteration in range (trainingIterations):
            output = self.think(trainingInputs)
            error = trainingOutputs - output
            adjustments = np.dot(trainingInputs.T, error * self.sigmoidDerivative(output))
            self.synapticWeights += adjustments

    def think(self, inputs):
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synapticWeights))
        print("This is the think function")
        return output

if __name__ == "__main__":
    neuralNetwork = NeuralNetwork()
    print("Random Synaptic Weights:")
    print(neuralNetwork.synapticWeights)

'''
#These are going to be the doubles input. We input 3 numbers and get
    #2X where X is the input.
    trainingInputs = np.array([[2,4,6],
                               [1,3,5],
                               [0,0,0],
                               [25,1111,1]])

    trainingOutputs = np.array([[4,8,12], [1,6,10], [0,0,0,], [50,2222,1]]).T



'''
#These are the correct inputs for the computer. These are the examples we want the computer
#to know are correct.
trainingInputs = np.array([[0,0,1],
                            [1,1,1],
                            [0,0,1],
                            [0,1,1]])
    #There are four outputs below because there are four variables here for it to test.
trainingOutputs = np.array([[0,1,0,0]]).T

neuralNetwork.train(trainingInputs, trainingOutputs, 5)
print("Synaptic Weights After Training")
print(neuralNetwork.synapticWeights)
A = str(input("input 1 "))
B = str(input("input 2 "))
C = str(input("input 3 "))

print ("New situation: Input data = ", A, B, C)
print ("Output Data:")
print(neuralNetwork.think(np.array([A,B,C])))