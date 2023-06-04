# Made by Kartik
flag = True
try:
    import torch.nn as nn

except ModuleNotFoundError:
    print("The module named torch  not installed, \n Install the torch version given in requirements.txt and then try agin.")
    flag =  False

if flag:


    class NeuralNet(nn.Module):
        """ This class gives our jarvis ability to think. Neural Network  """
        def __init__(self, input, hidden_size, num_out):
            super(NeuralNet, self).__init__()
            self.l1 = nn.Linear(input, hidden_size)                 # Input layer
            self.l2 = nn.Linear(hidden_size, hidden_size)           # Hidden layer
            self.l3 = nn.Linear(hidden_size, num_out)               # Output layer
            self.relucate = nn.ReLU()

        def forward(self, x):   # Not to change function name inherits in model training.
            """ This function connect x: Query to each layer of our Neural Network. """
            output = self.l1(x)
            output = self.relucate(output)         # Connecting each layer by framing neurons.
            output = self.l2(output)
            output = self.relucate(output)
            output = self.l3(output)
            return output
else:
    print(" ")


if __name__ == '__main__':
    pass
