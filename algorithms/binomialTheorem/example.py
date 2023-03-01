if __name__ == "__main__":
    n = 10 ** 9
    k = 2 * 10 ** 5
    mod = 10 ** 9 + 7
    f = genCombinationFunction(k, mod)
    print(f(n, k))
    print(f(10, 3))
    f = genO1CombinationFunction(10 ** 6, 998244353)
    print(f(10, 3))
