import sys

sys.setrecursionlimit(5000)


class Deck:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def horse_count(self, x, y):
        if x == self.n - 1 and y == self.m - 1:
            return 1
        if not (0 <= x < self.n and 0 <= y < self.m):
            return 0

        return (
            self.horse_count(x + 2, y - 1)
            + self.horse_count(x + 2, y + 1)
            + self.horse_count(x + 1, y + 2)
            + self.horse_count(x - 1, y + 2)
        )


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    print(Deck(n, m).horse_count(0, 0))
