import numpy as np


# N = (W - F + 2 * P) // STRIDE + 1
# input shape is [bz, h, w], type is np.array, cuz the mnist image is one-channel image instead of RGB

class Conv2d():
    '''input: [bz, h, w]
    '''
    def __init__(self, kernel=(3, 3), stride=1, padding=1, num_kernel=8) -> None:
        self.kernel_h, self.kernel_w = kernel.shape[0], kernel.shape[1]
        self.stride = stride
        self.padding = padding
        self.num_kernel = num_kernel
        self.kernel = np.random.randn(self.num_kernel, self.kernel_h, self.kernel_w) / 10 # initialization

    def forward(self, x):
        self.bz, self.h, self.w = x.shape[0], x.shape[1], x.shape[2]
        self.out_h = (self.h - self.kernel_h + self.padding * 2) // self.stride + 1
        self.out_w = (self.w - self.kernel_w + self.padding * 2) // self.stride + 1
        self.output = np.zeros((self.bz, self.out_h, self.out_w))

        out_h_index = 0
        for h_index in range(0, self.h, self.stride):
            out_w_index = 0
            for w_index  in range(0, self.w, self.stride):
                x_region = x[:, h_index:h_index + self.kernel_h, w_index:w_index + self.kernel_w]
                self.output[:, out_h_index, out_w_index] = np.sum(x_region * self.kernel, axis=(1, 2))

        return self.output


class BatchNorm2d():
    def __init__(self) -> None:
        pass

    def forward(self, x):
        return


class MaxPool2d():
    '''
    input: [bz, h, w]
    output: [bz, h', w']
    '''
    def __init__(self, kernel=(2, 2), stride=1) -> None:
        self.kernel_h, self.kernel_w = kernel.shape[0], kernel.shape[1]
        self.stride = stride

    def forward(self, x):
        self.bz, self.h, self.w = x.shape[0], x.shape[1], x.shape[2]
        self.out_h = (self.h - self.kernel_h) // self.stride + 1
        self.out_w = (self.w - self.kernel_w) // self.stride + 1
        self.output = np.zeros((self.bz, self.out_h, self.out_w))

        out_h_index = 0
        for h_index in range(0, self.h, self.stride):
            out_w_index = 0
            for w_index in range(0, self.w, self.stride):
                self.output[:, out_h_index, out_w_index] = \
                    np.max(x[:, h_index:h_index + self.kernel_h, w_index:w_index + self.kernel_w])
                out_w_index += 1
            out_h_index += 1

        return self.output


class CustomCNN():
    def __init__(self) -> None:
        pass

    def forward(self, x):
        return