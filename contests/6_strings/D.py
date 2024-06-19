def compute_prefix_function(s):
    n = len(s)
    pi = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j

    return pi


def kmp_search(alpha, beta):
    pi = compute_prefix_function(beta)
    j = 0
    occurrences = []

    for i in range(len(alpha)):
        while j > 0 and alpha[i] != beta[j]:
            j = pi[j - 1]
        if alpha[i] == beta[j]:
            j += 1
        if j == len(beta):
            occurrences.append(i - len(beta) + 1)
            j = pi[j - 1]

    return occurrences


if __name__ == "__main__":
    alpha = input()
    beta = input()

    positions = kmp_search(alpha, beta)

    print(len(positions), " ".join(map(lambda i: str(i + 1), positions)), sep="\n")
