import numpy as np

from data import train_loader, test_loader

if __name__ == '__main__':
    # load dataset
    root_dir = '/Users/neohuang/Downloads/data/mnist/'
    trainset = train_loader(datapath=root_dir+'train')
    print(trainset.shape)
    # testset = test_loader(datapath=root_dir+'test')