def fast_power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a

    if n % 2 == 0:
        return fast_power(a**2, n // 2)
    return a * fast_power(a, n - 1)


if __name__ == "__main__":
    print(fast_power(float(input()), int(input())))
