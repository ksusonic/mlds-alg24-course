def median(A, B):
    n = len(A)
    m = len(B)
    if n > m:
        return median(B, A)

    start = 0
    end = n
    realmidinmergedarray = (n + m + 1) // 2

    while start <= end:
        mid = (start + end) // 2
        leftAsize = mid
        leftBsize = realmidinmergedarray - mid

        leftA = A[leftAsize - 1] if (leftAsize > 0) else float("-inf")
        leftB = B[leftBsize - 1] if (leftBsize > 0) else float("-inf")
        rightA = A[leftAsize] if (leftAsize < n) else float("inf")
        rightB = B[leftBsize] if (leftBsize < m) else float("inf")

        if leftA <= rightB and leftB <= rightA:
            if (m + n) % 2 == 0:
                return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
            return max(leftA, leftB)

        elif leftA > rightB:
            end = mid - 1
        else:
            start = mid + 1


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    p = [[] for _ in range(n)]
    for i in range(n):
        p[i] = list(map(int, input().split()))

    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            print("%.5F" % median(p[i], p[j]))
