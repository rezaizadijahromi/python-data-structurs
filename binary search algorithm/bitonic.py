def find_highest_number(A):
    low = 0
    high = len(A)

    if len(A) < 3:
        return None

    while low <= high:
        mid = (low + high) // 2

        if mid-1 > 0:
            mid_left = A[mid - 1]
        else:
            mid_left = float("-inf")

        if mid+1 < len(A):
            mid_right = A[mid+1]
        else:
            mid_right = float("inf")

        if mid_left > A[mid] and mid_right < A[mid]:
            high = mid - 1

        elif mid_left < A[mid] and mid_right > A[mid]:
            low = mid + 1

        elif mid_left < A[mid] and A[mid] > mid_right:
            return A[mid]

        # print(A[mid])



A = [1,2,3,4,5,4,3,2,1]
A1 = [1,2,3,4,1]
A2 = [1,6,5,4,3,2,1]

x = find_highest_number(A1)
print(x)