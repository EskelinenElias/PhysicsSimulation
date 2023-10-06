import numpy
import math

A = numpy.array([[1, 2, 3], [4, 5, 6]])
B = numpy.zeros((2, 3))
for i in range(0, 2):
    for j in range(0, 3):
        B[i][j]=math.atan2(A[i][j], A[i][j])


print(numpy.arctan2(A, A))
print(B)

