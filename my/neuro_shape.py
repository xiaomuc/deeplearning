# coding: utf-8
import neuro as nu

x, _ = nu.get_data()
network = nu.init_network()
W1, W2, W3 = network['W1'], network['W2'], network['W3'] 

print("x",x.shape)
print("x[0]",x[0].shape)
print("W1",W1.shape)
print("W2",W2.shape)
print("W3",W3.shape)
