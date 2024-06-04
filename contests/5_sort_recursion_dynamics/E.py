def bsearch(n, f):
    low = 1
    high = 2
    while f(high) <= n:
        low, high = high, 2 * high

    while low < high - 1:
        mid = (low + high) // 2
        assert low < mid < high
        if f(mid) <= n:
            low = mid
        else:
            high = mid

    return low


def seq_func(n):
    return (
        bsearch(n, lambda i: i**2)
        + bsearch(n, lambda i: i**3)
        - bsearch(n, lambda i: i**6)
    )


if __name__ == "__main__":
    x = int(input())
    if x == 1:
        print(1)
    else:
        print(bsearch(x - 1, seq_func) + 1)
