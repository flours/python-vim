
# 最も近い値が欲しい時のラップ
def binary_search_find_closest(data, target):
    idx = binarySearch(data, target, 0, len(data) - 1)
    if idx == len(data) - 1:
        return idx
    if abs(target - data[idx]) > abs(target - data[idx + 1]):
        return idx + 1
    return idx


if __name__ == "__main__":
    arr = [101, 102, 103, 104, 105, 106]
    print("102のインデックスは", binarySearch(arr, 102, 0, len(arr) - 1))  # 1
    arr = [101, 102, 103, 104, 106, 107]
    print("105を超えない最大のインデックスは", binarySearch(arr, 105, 0, len(arr) - 1))  # 3

    print("10を超えない最大のインデックスはないので0が帰ります", binarySearch(arr, 10, 0, len(arr) - 1))  # 0
    print("つまり最小より値が小さい場合は0,それ以外の場合はその値以下の最大の値を探索します。")
    print("最大より値が大きい場合は最後のindexが帰ります")
