from turtle import forward
import numpy as np

class BatchNorm2d():
    def __init__(self, eps = 0.001, momentum = 0.99, beta = 0, gamma = 1) -> None:
        self.eps = eps
        self.momentum = momentum
        self.beta = beta
        self.gamma = gamma
        self.training_mean = 0.0
        self.training_var = 1.0

    def forward_train(self, input):
        # input is [bz, c, h, w]
        self.mean = input.mean(axis = 0)
        self.var = input.var(axis = 0)
        input_norm = (input - self.mean) / (self.var + self.eps)
        res = self.gamma * input_norm + self.beta

        self.training_mean = self.momentum * self.mean + (1 - self.momentum) * self.mean
        self.training_var = self.momentum * self.var + (1 - self.var) * self.var

        return res

    def forward_inference(self, input):
        input_norm = (input - self.training_mean) / (self.training_var + self.eps)
        res = self.gamma * input_norm + self.beta
        return res