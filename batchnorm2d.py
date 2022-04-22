import numpy as np

class BatchNorm2d():
    def __init__(self, eps = 0.001, gamma = 1, beta = 0, momentum = 0.99) -> None:
        self.eps = eps
        self.gamma = gamma
        self.beta = beta
        self.momentum = momentum
        self.running_mu = 0.0
        self.running_var = 1.0
    
    def forward_train(self, input):
        '''
        input: [bz, c, h, w]
        '''
        # calculate mean and variance of batch
        mu = input.mean(axis = 0)
        var = input.var(axis = 0)
        # norm
        input_norm = (input - mu) / np.sqrt(var + self.eps)
        # scale and shift
        res = self.gamma * input_norm + self.beta

        # update
        self.running_mu = self.running_mu * self.momentum + (1 - self.momentum) * mu
        self.running_var = self.running_var * self.momentum + (1 - self.momentum) * var
        return res

    def forward_test(self, input):
        input_norm = (input - self.running_mu) / np.sqrt(self.running_var + self.eps)
        res = self.gamma * input_norm + self.beta
        return res