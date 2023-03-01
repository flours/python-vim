# 2次元リストlに対してF2上でガウス・ジョルダン法による掃き出し法
# l 変換する連立方程式の行列 l2 答えの行列
def F2sweep(l):
    cnt = 0
    for i in range(len(l[0])):
        # 0じゃないところを上に持ってくる
        for j in range(cnt, len(l)):
            if l[j][i] != 0:
                l[cnt], l[j] = l[j], l[cnt]
                break
        if l[cnt][i] == 0:
            continue
        # この時点ですでに1なので割り算はいらない
        for j in range(len(l)):
            if j == cnt:
                continue
            if l[j][i] != 0:
                for k in range(len(l[cnt])):
                    l[j][k] -= l[cnt][k]
                    l[j][k] %= 2
        cnt += 1
        if cnt == len(l):
            break
    return l


def rank(l):
    rank = 0
    for i in l:
        if sum(i):
            rank += 1
    return rank
