def main(l: list):
    if not l:
        return
    max_sum = None
    curr_sum = curr_start = start = end = 0

    for i, n in enumerate(l):
        if curr_sum + n <= n:
            curr_sum = n
            curr_start = curr_end = i
        else:
            curr_sum += n
            curr_end = i
        if max_sum is None or curr_sum > max_sum:
            start, end = curr_start, curr_end
            max_sum = curr_sum

    return start, end


if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split()))
    res = main(l)
    print(*res)
