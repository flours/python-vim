def ABC279D():
    A,B=map(int,input().split())

    import math
    def f(g):
        ret=g*B-B
        ret+=A/math.sqrt(g)
        return ret

    ret=int(TemarySearch(f, 1, 10**18))
    print(min(f(ret),f(max(ret-1,1)),f(ret+1)))
