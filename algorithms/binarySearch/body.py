def binarySearch(X, target, left, right):
    while True:
        mid = (left + right) // 2
        if X[left] > target:
            return left
        if X[right] <= target:
            return right
        if left == right:
            return left
        if X[mid] > target:
            right = mid - 1
        else:
            left = mid
            right = right - 1
