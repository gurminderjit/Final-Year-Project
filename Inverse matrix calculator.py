import numpy as np

# Define the matrix A
A = np.array([[1., 1., 1., 1.], 
              [-1., 1., 0., 0.],
              [0., -1., 1., 0.],
              [0., 0., -1., 1.] 
              ])

# Calculate the inverse of A
A_inv = np.linalg.inv(A)

print("Matrix A:\n", A)
print("Inverse of A:\n", A_inv)
