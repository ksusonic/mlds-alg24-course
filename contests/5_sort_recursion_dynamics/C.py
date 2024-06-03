def solution(p, w) -> tuple[int, int, list[int]]:
    dp = [0] * (w + 1)
    selected = [[] for _ in range(w + 1)]

    for i, r in enumerate(p):
        for j in range(w, r - 1, -1):
            if dp[j - r] + r > dp[j]:
                dp[j] = dp[j - r] + r
                selected[j] = selected[j - r] + [i]

    return dp[w], len(selected[w]), [p[i] for i in selected[w]]


if __name__ == "__main__":
    n, w = int(input()), int(input())
    p = list(map(int, input().split()))

    res_a, res_m_len, res_m = solution(p, w)
    print(res_a)
    print(res_m_len)
    print(*res_m)
