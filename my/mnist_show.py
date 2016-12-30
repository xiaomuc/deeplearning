# coding: utf-8
import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
   pil_img = Image.fromarray(np.uint8(img))
   pil_img.show()
   
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
print("x_train len",len(x_train))
args = sys.argv
index=int(args[1])
print("index",index)
img=x_train[index]
label=t_train[index] 
print(label)

print(img.shape)
img = img.reshape(28,28)
print(img.shape)

img_show(img)