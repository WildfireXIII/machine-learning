import NNetDemo as net

nn = net.NeuralNetwork(2,1,3,1)
nn.initTheanoFunctions()
nn.readTrainingData("data.txt")

nn.generateWeights()
nn.runFeedForward([[1.0,0.0]])
nn.backPropogate([[1.0]]);
