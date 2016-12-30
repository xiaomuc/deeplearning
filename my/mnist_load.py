# coding: utf-8
import sys,os
sys.path.append(os.pardir)  #親ディレクトリのファイルをインポートするための設定
from dataset.mnist import load_mnist

#最初は数分待ちが発生する
(x_train, t_train),(x_test, t_test) = load_mnist(flatten=True,normalize=False)

#それぞれのデータの形状を出力
print("x_train",x_train.shape)
print("t_train",t_train.shape)
print("x_test",x_test.shape)
print("t_test",t_test.shape)
