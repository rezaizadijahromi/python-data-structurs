data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = int(input())


def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

def binary_search_iterative(data, tartget):
    low = 0
    high = len(data)

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True

        elif target > data[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return False


def binary_search_recursive(data, target, low, high):
    if low > high:
        return False

    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True

        elif target > data[mid]:
            return binary_search_recursive(data, target, mid + 1, high)
        else:
            return binary_search_iterative(data, target, low, mid-1)

def find_closest_num(A, target):
    low = 0
    high = len(A) 
    min_diff = float("inf")
    closest = None

    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]

    while low <= high:
        mid = (low+high) // 2

        if mid + 1 < len(A):
            min_diff_right = abs(A[mid+1] - target)
        elif mid > 0:
            min_diff_left = abs(A[mid-1] - target)

        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest = A[mid-1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest = A[mid+1]

        if A[mid] > target:
            high = mid - 1
        elif target > A[mid]:
            low = mid + 1
        else:
            return A[mid]

    return closest


def find_fixed_num(A):
    low = 0
    high = len(A)

    while low <= high:
        mid = (low+high) // 2

        if A[mid] > mid:
            high = mid - 1
        elif A[mid] < mid:
            low = mid + 1

            
