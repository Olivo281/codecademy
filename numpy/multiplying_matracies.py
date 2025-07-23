import numpy as np

first = np.array([[2, -3, 1], [-2, -1, 4], [0,2,2]])
second = np.array([[3, -2, 1], [1, -1, 2], [-2, 2, 0]])
print(first @ second)

g1 = np.array([[2, -3,1], [3, 1, 1],[-1,-2,-1]])
g2 = np.array([2,-1, 1])

print(np.linalg.solve(g1, g2))

c1 = np.array([3,-1,2])
c2 = np.array([0,-1,1])

dot_product = np.dot(c1, c2)    
norm_a = np.linalg.norm(c1)
norm_b = np.linalg.norm(c2)

cosine = dot_product / (norm_a * norm_b)

angle = np.degrees(np.arccos(cosine))
print(angle)