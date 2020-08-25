def find_fixed_point_linear(A):
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
    return None


def find_fixed_point(A):
    low = 0 
    high = len(A)

    while low <= high:
        mid = (low + high) // 2

        if A[mid] < mid:
            low = mid + 1
        elif A[mid] > mid:
            high = mid - 1

        else:
            return A[mid]

    return None


A = [-10, -5, 0, 3, 7]
A1 = [0, 2, 5, 8, 17]
print(find_fixed_point(A1))