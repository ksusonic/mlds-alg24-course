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


if __name__ == '__main__':
    _ = int(input())
    sorted_palindrome = quicksort(list(input()))
    d = dict()
    # d будет отсортированный словарь, тк
    # вставляли в него в отсортированном порядке
    for i in sorted_palindrome:
        d[i] = d.get(i, 0) + 1

    single = None
    half = []
    for k, v in d.items():
        if v // 2 > 0:
            half.append(k * (v // 2))
        elif v == 1 and single is None:
            single = k

    for i in half:
        print(i, end='')
    if single is not None:
        print(single, end='')
    for i in range(len(half), 0, -1):
        print(half[i - 1], end='')
