def main(l: list):
    cur = l[0]
    cnt = 0
    for n in l:
        if cur == n:
            cnt += 1
        else:
            if cnt == 1:
                cur = n
            else:
                cnt -= 1
    return cur


if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split()))
    res = main(l)
    print(res)
