import os
from PIL import Image
import numpy as np


def train_loader(datapath):
    res = []
    for filename in os.listdir(datapath):
        if '.' in filename:
            continue
        filename = os.path.join(datapath, filename)
        for imgname in os.listdir(filename):
            imgpath = os.path.join(filename, imgname)
            img = Image.open(imgpath)
            img = np.array(img) # PIL --> np.array; size is [28, 28]
            res.append(img)
            if len(res) == 1000:
                res = np.array(res)
                return res
    res = np.array(res)
    return res


def test_loader(datapath):
    res = []
    for filename in os.listdir(datapath):
        if '.' in filename:
            continue
        filename = os.path.join(datapath, filename)
        for imgname in os.listdir(filename):
            imgpath = os.path.join(filename, imgname)
            img = Image.open(imgpath)
            img = np.array(img) # PIL --> np.array; size is [28, 28]
            res.append(img)
            if len(res) == 1000:
                res = np.array(res)
                return res
    res = np.array(res)
    return res
