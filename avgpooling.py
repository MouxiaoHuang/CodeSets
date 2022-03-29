import numpy as np

def AvgPool2d(featuremap, size, stride):
    channel, height, width = featuremap.shape[0], featuremap.shape[1], featuremap.shape[2]
    out_height, out_width = (height - size) // stride + 1, (width - size) // stride + 1
    output = np.zeros((channel, out_height, out_width), dtype=np.uint8)

    for c_index in range(channel):
        h_index = 0
        for h in range(0, height, stride):
            w_index = 0
            for w in range(0, width, stride):
                try:
                    output[c_index, h_index, w_index] = np.mean(featuremap[c_index, h : h + size, w : w + size])
                except:
                    break
                w_index += 1
            h_index += 1
    return output

if __name__ == '__main__':
    feat = np.arange(1, 28).reshape((3,3,3))
    print(feat)
    feat_maxpool = AvgPool2d(feat, 2, 1)
    print(feat_maxpool)