from math import sqrt

if __name__ == "__main__":
    C = float(input())
    l, r, eps = 0, C, 1e-7
    while r - l > eps:
        m = (l + r) / 2
        if m * m + sqrt(m) > C:
            r = m
        else:
            l = m
    print("{:.7f}".format(l))
