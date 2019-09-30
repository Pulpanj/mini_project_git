import numpy as np
# smearing matrix
A = np.array(([0.5,0.5,0],[0,0.5,0.5],[0,0,0.5]))
print(A)

# original image
b=np.array([2,3,2])
print ('observed')
# observer image
c=A.dot(b)
print(c)
# reconstructed image
A_inv = np.linalg.inv(A)
print(A_inv)
print ('observed')
x=A_inv.dot(c)
print(x)