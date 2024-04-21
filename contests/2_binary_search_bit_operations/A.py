def main(l1: list, l2: list):
    for x in l2:
        low, high, result = 0, len(l1), -1
        while low < high:
            mid = (low + high) // 2
            if l1[mid] < x:
                low = mid + 1
            elif l1[mid] > x:
                high = mid
            else:
                result = mid
                high = mid
        lower = result + 1
        if lower == 0:
            print(0)
            continue

        low, high, result = 0, len(l1), -1
        while low < high:
            mid = (low + high) // 2
            if l1[mid] < x:
                low = mid + 1
            elif l1[mid] > x:
                high = mid
            else:
                result = mid
                low = mid + 1
        upper = result + 1
        print(lower, upper)


if __name__ == "__main__":
    n, m = map(int, input().split())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    main(l1, l2)
