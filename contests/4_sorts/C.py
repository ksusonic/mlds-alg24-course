def quicksort(s: list) -> list:
    if len(s) <= 1:
        return s

    less = []
    equal = []
    greater = []

    pivot = s[0]
    for i in range(0, len(s)):
        if s[i] < pivot:
            less.append(s[i])
        elif s[i] == pivot:
            equal.append(s[i])
        else:
            greater.append(s[i])

    return quicksort(less) + equal + quicksort(greater)


def formula(r, g, b) -> int:
    return (r - g) ** 2 + (g - b) ** 2 + (r - b) ** 2


def solution(red, green, blue) -> [int, int, int]:
    r, g, b = 0, 0, 0
    current_baseline = formula(red[r], green[g], blue[b])
    result = [red[r], green[g], blue[b]]

    while r < len(red) or g < len(green) or b < len(blue):
        next_diffs = [
            formula(red[r + 1], green[g], blue[b]) if r < len(red) - 1 else float("inf"),
            formula(red[r], green[g + 1], blue[b]) if g < len(green) - 1 else float("inf"),
            formula(red[r], green[g], blue[b + 1]) if b < len(blue) - 1 else float("inf"),
        ]

        min_val = min(next_diffs)
        if min_val == float('inf'):
            return result

        min_index = next_diffs.index(min_val)
        if min_index == 0:
            r += 1
        elif min_index == 1:
            g += 1
        else:
            b += 1

        if next_diffs[min_index] < current_baseline:
            current_baseline = next_diffs[min_index]
            result = [red[r], green[g], blue[b]]

    return result


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        line = input()
        if not line:
            _ = input()

        # SORTED!
        r, g, b = [quicksort(list(map(int, input().split()))) for i in range(3)]

        print(*solution(r, g, b))
