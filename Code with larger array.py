import numpy as np

# Define the number of risky routes and the expected conditions of the routes
n = 6
mu_1 = 0.1
mu_2 = 0.2
mu_3 = 0.3
mu_4 = 0.4
mu_5 = 0.5
mu_6 = 0.6
mu_7 = 0.7
mus = np.array([mu_1, mu_2, mu_3, mu_4, mu_5, mu_6, mu_7])

# Construct the coefficient matrix and constant vector
A = np.zeros((n+1, n+1))
b = np.zeros(n+1)
for j in range(n+1):
        A[0][j] = 1
        b[0]=1
for i in range(1,n+1):
    for j in range(n+1):
      if j == i-1:
        A[i][j] = -1
      elif j == i:
        A[i][j] = 1
      else:
        A[i][j] = 0
    b[i] = mus[i]-mus[i-1]

print(A)

print(b)
# Solve the linear equations
x = np.linalg.solve(A, b)

# Print the solution
print(x)

