if __name__ == '__main__':
    n = int(input())
    press = [int(i) for i in input().split()]
    k = int(input())

    press_count = {}

    for i in [int(li) for li in input().split()]:
        press_count[i] = press_count.get(i, 0) + 1
    for i in range(n):
        if press[i] < press_count[i + 1]:
            print("yes")
        else:
            print("no")
