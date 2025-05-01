import numpy as np
ket0 = np.array([[1], [0]])
ket1 = np.array([[0], [1]])

H_Gate = np.array([[1,1], [1,-1]]) / np.sqrt(2)
Out1 = H_Gate @ ket0
Out2 = H_Gate @ ket1

print(Out1)
print(Out2)