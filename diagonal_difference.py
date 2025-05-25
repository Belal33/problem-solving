# Given a square matrix, calculate the absolute difference between the sums of its diagonals.diagonalDifference
arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]


def diagonal_difference(arr: list[list[int]]):
    n = len(arr)
    l: int = 0
    r: int = 0
    #######################
    #  1,1              1,n
    #      2,2    2,n-1
    # 	   3,n-2  3,3
    #  n,1             n,n
    #######################
    for i in range(n):
        l += arr[i][i]
        r += arr[i][n - i - 1]
    df = abs(l - r)
    return df


print(diagonal_difference(arr))
