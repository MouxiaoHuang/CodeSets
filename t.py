from turtle import forward
import numpy as np

class BatchNorm2d():
    def __init__(self, eps=0.001, gamma=1, beta=0.1, momentum=0.99) -> None:
        self.eps = eps
        self.gamma = gamma
        self.beta = beta
        self.momentum = momentum
        self.running_mean = 0.0
        self.running_var = 1.0

    def forward_train(self, input):
        '''
        input: [bz, c, h, w]
        '''
        # cal mean and var
        mu = input.mean(axis=0)
        var = input.var(axis=0)
        # norm
        input_norm = (input - mu) / np.sqrt(var + self.eps)
        # scale and shift
        res = self.gamma * input_norm + self.beta
        # update
        self.running_mean = self.momentum * self.running_mean + (1 - self.momentum) * mu
        self.running_var = self.momentum * self.running_var + (1 - self.momentum) * var
        return res

    def forward_test(self, input):
        input_norm = (input - self.running_mean) / np.sqrt(self.running_var + self.eps)
        res = self.gamma * input_norm + self.beta
        return res


class MaxPool2d():
    def __init__(self, kernel_size=(2, 2), stride=1) -> None:
        self.kernel_size_h = kernel_size[0]
        self.kernel_size_w = kernel_size[1]
        self.stride = stride

    def forward(self, x):
        self.channel, self.height, self.width = x.shape[0], x.shape[1], x.shape[2]
        self.out_h = (self.height - self.kernel_size_h) // self.stride + 1
        self.out_w = (self.width - self.kernel_size_w) // self.stride + 1
        self.output = np.zeros((self.channel, self.out_h, self.out_w), dtype=np.uint8)
        
        for c in range(self.channel):
            h_index = 0
            for h in range(0, self.height, self.stride):
                w_index = 0
                for w in range(0, self.width, self.stride):
                    try:
                        self.output[c, h_index, w_index] = np.max(x[c, h : h + self.kernel_size_h, w : w + self.kernel_size_w])
                    except:
                        break
                    w_index += 1
                h_index += 1
        return self.output

maxpool = MaxPool2d(kernel_size=(2, 1), stride=1)
x = np.arange(1, 28).reshape((3, 3, 3))
output = maxpool.forward(x)
print(x)
print(output)