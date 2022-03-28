
import numpy as np

def maxpooling(featuremap, size, stride):
    channel, height, width = featuremap.shape[0], featuremap.shape[1], featuremap.shape[2]
    out_height = (height - size) // stride + 1
    out_width = (width - size) // stride + 1
    out_maxpool = np.zeros((channel, out_height, out_width), dtype=np.uint8)

    for c in range(channel):
        out_h_index = 0
        for h in range(0, out_height, stride):
            out_w_index = 0
            for w in range(0, out_width, stride):
                try:
                    out_maxpool[c, out_h_index, out_w_index] = np.max(featuremap[c, h : h + size, w : w + size])
                except:
                    break
                out_w_index += 1
            out_h_index += 1
    return out_maxpool

if __name__ == '__main__':
    feat = np.arange(1, 28).reshape((3,3,3))
    feat_maxpool = maxpooling(feat, 2, 1)
    print(feat_maxpool)