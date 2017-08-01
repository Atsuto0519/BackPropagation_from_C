import numpy as np

def func_sigmoid(X, alpha) :
    res = []
    for x in X :
        res.append(1/(1+np.exp(alpha*x)))

    return res

alpha = -4.0
# x1=0, x2=0のときのXOR
x = [0.0, 0.0]
w = [[-1.31,-1.31], [-1.69,-1.70], [2.74,-2.78]]
b = [1.96, 0.71, -1.31]

o_b = func_sigmoid([np.dot(x, w[0])+b[0]], alpha)
o_c = func_sigmoid([np.dot(x, w[1])+b[1]], alpha)
x_j = []
x_j.extend(o_b)
x_j.extend(o_c)
o_a = func_sigmoid([np.dot(x_j, w[2])+b[2]], alpha)

print("X")
print(x)
print("o_b")
print(o_b)
print("o_c")
print(o_c)
print("o_a")
print(o_a)
