import math

pi = 3.142857
m = 8
n = 8


# Function to find discrete cosine transform
def dct_transform(matrix):
    # The vector dct is created to store the discrete cosine transform in the near future
    dct = []
    for i in range(m):
        dct.append([None for _ in range(n)])

    # Iterating the given matrix
    for i in range(m):
        for j in range(n):
            # ci and cj depend on the frequency and the number of rows and columns of the given matrix
            if i == 0:
                ci = 1 / (m ** 0.5)
            else:
                ci = (2 / m) ** 0.5
            if j == 0:
                cj = 1 / (n ** 0.5)
            else:
                cj = (2 / n) ** 0.5

            # The variable s is created to temporarily store the sum of cosine signals
            s = 0
            # Again, the matrix is iterated
            for k in range(m):
                for p in range(n):
                    # For every iteration, the DCT is computed
                    dct1 = matrix[k][p] * math.cos((2 * k + 1) * i * pi / (
                            2 * m)) * math.cos((2 * p + 1) * j * pi / (2 * n))
                    s = s + dct1

            dct[i][j] = ci * cj * s

    # The matrix dct is printed with the results of the discrete cosine transform
    for i in range(m):
        for j in range(n):
            print(dct[i][j], end="\t")
        print()


# A given matrix to test the result
M = [[255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255]]
# Calling the function with the previous matrix to test the program
dct_transform(M)
