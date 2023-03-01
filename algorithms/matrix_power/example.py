if __name__ == "__main__":
    print("フィボナッチ数列の第N項をを行列累乗で計算します")
    mod = 10 ** 9 + 7
    l = [[0, 1], [1, 1]]
    init = [[0, 1]]

    N = 21
    ans = mat_mul(init, mat_pow(l, N, mod), mod)
    print(f"第{N}項", ans[0][0] % mod)
    N = 100
    ans = mat_mul(init, mat_pow(l, N, mod), mod)
    print(f"第{N}項", ans[0][0] % mod)
    N = 10 ** 18
    ans = mat_mul(init, mat_pow(l, N, mod), mod)
    print(f"第{N}項(mod{mod})", ans[0][0] % mod)
