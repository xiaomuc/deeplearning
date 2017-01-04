# coding: utf-8
import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
   pil_img = Image.fromarray(np.uint8(img))
   pil_img.show()
   
def show28(img):
    img_show(img.reshape(28,28))
   
def main():
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
    print("x_train len",len(x_train))
    args = sys.argv
    if len(args)<2:
        print("you can set index as parameter:")
        print("python",args[0],"[index]")
        index=0
    else:
        index=int(args[1])
    print("index",index)
    img=x_train[index]
    label=t_train[index] 
    print(label)

    show28(img)
    
if __name__ == '__main__':
    main()    