from bisect import bisect


def solution(matrix: list[list[int]], k: int) -> int:
    n = len(matrix)
    left, right = matrix[0][0], matrix[n - 1][n - 1]

    res = matrix[0][n - 1]
    while left < right:
        mid = (left + right) >> 1
        count = 0
        for i in matrix:
            count += bisect(i, mid)

        if count < k:
            left = mid + 1
        else:
            res = mid
            right = mid

    return res


if __name__ == "__main__":
    n, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print(solution(matrix, k))
