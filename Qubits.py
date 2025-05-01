import numpy as np
ket0 = np.array([[1], [0]])
ket1 = np.array([[0], [1]])

ket_plus = (ket0 + ket1) / np.sqrt(2)
print(ket_plus)