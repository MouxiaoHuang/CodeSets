import numpy as np

class MaxPool2d():
    def __init__(self, kernel_size = (2, 2), stride = 1) -> None:
        self.stride = stride
        self.kernel_size_h = kernel_size[0]
        self.kernel_size_w = kernel_size[1]

    def forward(self, x):
        self.channel, self.height, self.width = x.shape[0], x.shape[1], x.shape[2]
        self.out_h = (self.height - self.kernel_size_h) // self.stride + 1
        self.out_w = (self.width - self.kernel_size_w) // self.stride + 1
        self.output = np.zeros((self.channel, self.out_h, self.out_w), dtype=np.uint8)

        for c_index in range(self.channel):
            out_h_index = 0
            for h_index in range(0, self.height, self.stride):
                out_w_index = 0
                for w_index in range(0, self.width, self.stride):
                    try:
                        self.output[c_index, out_h_index, out_w_index] = np.max(x[c_index, h_index : h_index + self.kernel_size_h, w_index : w_index + self.kernel_size_w])
                    except:
                        break
                    out_w_index += 1
                out_h_index += 1
        return self.output

maxpool = MaxPool2d(kernel_size=(2, 1), stride=1)
x = np.arange(1, 28).reshape((3, 3, 3))
output = maxpool.forward(x)
print(x)
print(output)