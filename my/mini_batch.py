# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
from dataset.mnist import load_mnist
import mnist_show as sw

def cross_entropy_error_one(y, t, one_hot=True):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshpae(1, y.size)
    
    batch_size = y.shpae[0]
    if one_hot:
        return -np.sum(t * np.log(y) / batch_size)
    else:
        return -np.sum(t * np.log(y[np.arange(batch_size)]) / batch_size)
       
def main():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)
    print("x_train",x_train.shape)
    print("t_train",t_train.shape)

    train_size = x_train.shape[0]
    print("train_size",train_size)
    batch_size = 10
    print("batch_size",batch_size)
    batch_mask = np.random.choice(train_size, batch_size)
    print("batch_mask",batch_mask)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    print(t_batch)    
 

if __name__ == '__main__':
    main()