def lcs(s1: str, s2: str) -> tuple[int, str]:
    LCS = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            LCS[i][j] = max(
                LCS[i-1][j],
                LCS[i][j-1],
                LCS[i-1][j-1] + (s1[i-1] == s2[j-1])
            )

    ans = []
    i, j = len(s1), len(s2)

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            ans.append(s1[i - 1])
            i -= 1
            j -= 1
        elif LCS[i - 1][j] > LCS[i][j - 1]:
            i -= 1
        else:
            j -= 1
    

    return LCS[len(s1)][len(s2)], ''.join(reversed(ans))
