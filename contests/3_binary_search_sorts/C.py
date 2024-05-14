if __name__ == "__main__":
    n = int(input())
    dl, c = 1, 9

    while n > dl * c:
        n -= dl * c
        dl += 1
        c *= 10

    start = 10 ** (dl - 1)
    num = start + (n - 1) // dl
    di = (n - 1) % dl
    print(int(str(num)[di]))
