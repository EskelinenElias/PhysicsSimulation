import numpy as np

def implies(p: np.ndarray, q: np.ndarray) -> np.ndarray: 
    if p.shape == q.shape: 
        shape = p.shape
        r = np.zeros(shape = shape)
        for i in range(shape[0]):
            for j in range(shape[1]): 
                if p[i][j]:
                    if q[i][j]: 
                        r[i][j] = True
                    else: 
                        r[i][j] = False
                else: 
                    r[i][j] = True
        return r
    return None

p = np.array([[0, 0, 1, 1]]).transpose()
q = np.array([[0, 1, 0, 1]]).transpose()
p.shape
left = np.logical_and(p, q)
right = np.logical_or(p, np.logical_not(q))
result = implies(left, right)
print(p)
print(q)
print(left)
print(right)
print(implies(left, right))

left2 = np.logical_not(np.logical_and(p, q))
print(left2)
left3 = np.logical_or(np.logical_not(p), np.logical_not(q))
print(left3)
if np.array_equal(left2, left3): print("logical equivalence has been accomplished!")
print(np.logical_or(left2, right))


end = "    "
print("p" + end + "q" + end + "L" + end + "R" + end + "r")
for i in range(4): 
    print(int(p[i][0]), end = end)
    print(int(q[i][0]), end = end)
    print(int(left[i][0]), end = end)
    print(int(right[i][0]), end = end)
    print(int(result[i][0]))

