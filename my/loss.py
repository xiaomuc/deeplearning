# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)
    
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))
    
print("損失関数")
t = [0,0,1,0,0,0,0,0,0,0]
print("教師",t)

y1 = [0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]
print("y1(2=0.6)",y1)
y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print("y2(7=0.6)",y2)

print("二乗和誤差")
print("y1",mean_squared_error(np.array(y1),np.array(t)))
print("y2",mean_squared_error(np.array(y2),np.array(t)))

print("交差エントロピー誤差")
print("y1",cross_entropy_error(np.array(y1),np.array(t)))
print("y2",cross_entropy_error(np.array(y2),np.array(t)))
