def main(l: list):
    n = len(l) + 1
    sum = n * (n + 1) // 2
    for v in l:
        sum -= v
    return sum


if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split()))
    res = main(l)
    print(res)

# TESTS
assert main([1, 2, 4, 5, 6]) == 3
