def preprocess(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    m = len(matrix[0])
    prefix_sums = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            prefix_sums[i + 1][j + 1] = (
                matrix[i][j]
                + prefix_sums[i][j + 1]
                + prefix_sums[i + 1][j]
                - prefix_sums[i][j]
            )
    return prefix_sums


def query(prefix_sums: list[list[int]], x1: int, y1: int, x2: int, y2: int) -> int:
    return (
        prefix_sums[x2][y2]
        - prefix_sums[x1 - 1][y2]
        - prefix_sums[x2][y1 - 1]
        + prefix_sums[x1 - 1][y1 - 1]
    )


if __name__ == "__main__":
    n, m, q = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    prefix_sums = preprocess(matrix)
    for _ in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        print(query(prefix_sums, x1, y1, x2, y2))
