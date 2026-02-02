# %% [markdown]
# 1. Create a vector with values ranging from 10 to 49.
# 2. Create a 3x3 matrix with values ranging from 0 to 8.
# 3. Create a 3x3 identity matrix.
# 4. Create a 3x3x3 array with random values.
# 5. Create a 10x10 array with random values and find the minimum and maximum values.
# 6. Create a random vector of size 30 and find the mean value.
# 7. Normalize a 5x5 random matrix.
# 8. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product).
# 9. Create two 3x3 matrices and compute their dot product.  
# 10. Given a 4x4 matrix, find its transpose.  
# 11. Create a 3x3 matrix and calculate its determinant.  
# 12. Create two matrices \( A \) (3x4) and \( B \) (4x3), and compute the matrix product \( A \cdot B \).  
# 13. Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product.  
# 14. Solve the linear system \( Ax = b \) where \( A \) is a 3x3 matrix, and \( b \) is a 3x1 column vector.  
# 15. Given a 5x5 matrix, find the row-wise and column-wise sums.

# %%
pip install numpy

# %%
import numpy as np

# %%
np.arange(10, 50)

# %%
a3d = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
])

# %%
a3d.shape

# %%
np.eye(3, dtype=int)

# %%
arr = np.random.rand(3, 3, 3)
arr

# %%
arr.shape

# %%
arr10 = np.random.rand(10, 10)
arr10

# %%
arr10.max()

# %%
arr10.min()

# %%
vect = np.random.rand(30)
vect

# %%
vect.mean()

# %%
x = np.random.rand(5, 5)
xnorm = (x - x.min()) / (x.max() - x.min())
print(xnorm)

# %%
A = np.random.randint(0, 6, (5, 3))
B = np.random.randint(0, 6, (3, 2))

C = A @ B
print(C)

# %%
D = np.random.randint(0, 6, (3, 3))
E = np.random.randint(0, 6, (3, 3))

F = D.dot(E)
F

# %%
D = np.random.randint(0, 6, (4, 4))
D

# %%
D.T

# %%
D = np.random.randint(0, 6, (3, 3))
D

# %%
np.linalg.det(D)

# %%
A = np.random.randint(0, 6, (3, 4))
B = np.random.randint(0, 6, (4, 3))

F = A @ B
F

# %%
D = np.random.randint(0, 6, (3, 3))
V = np.random.randint(0, 6, (3))
V


# %%
D * V

# %%
A = np.random.randint(0, 6, (5, 3))
B = np.random.randint(0, 6, (3, 2))

C = A @ B
print(C)

# %%
D = np.random.randint(0, 6, (3, 3))
V = np.random.randint(0, 6, (3, 1))

X = np.linalg.solve(D, V)
X

# %%
A = np.random.randint(0, 6, (5, 5))
A

# %%
rows_sums = A.sum(axis=1)
rows_sums

# %%
column_sums = A.sum(axis=0)
column_sums

# %%



