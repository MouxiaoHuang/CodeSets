from turtle import forward, shape
import numpy as np

# N = (W - F + 2 * P) / S + 1
# 暂时有点bug

class Conv2d():
    def __init__(self, kernel = np.ones([3, 3]), padding = 0, stride = 1) -> None:
        # kernel: [h, w]
        self.kernel = kernel
        self.kernel_size_h = kernel.shape[0]
        self.kernel_size_w = kernel.shape[1]
        self.padding = padding
        self.stride = stride

    def forward(self, input):
        '''input: [c, h, w]
        '''
        self.c, self.h, self.w = input.shape[0], input.shape[1], input.shape[2]
        self.out_h = (self.h - self.kernel_size_h + 2 * self.padding) // self.stride + 1
        self.out_w = (self.w - self.kernel_size_w + 2 * self.padding) // self.stride + 1
        self.output = np.zeros((self.c, self.out_h, self.out_w), dtype=np.uint8)

        for c_i in range(self.c):
            out_h_i = 0
            for h_i in range(0, self.h, self.stride):
                out_w_i = 0
                for w_i in range(0, self.w, self.stride):
                    region = input[c_i, h_i : self.kernel_size_h, w_i : self.kernel_size_w]
                    print(region.shape)
                    self.output[c_i, out_h_i, out_w_i] = (region * self.kernel).sum()
                    out_w_i += 1
                out_h_i += 1
        return self.output

img = [[[0, 50, 0, 29], [0, 80, 31, 2], [33, 90, 0, 75], [0, 9, 0, 95]]]
img = np.array(img)
ker = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
conv = Conv2d(kernel=ker, padding=0, stride=1)
output = conv.forward(img)
print(output)