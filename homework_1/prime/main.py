def sieve(n: int) -> list[int]:
    if n <= 1:
        return []

    ans = [1] * (n + 1)
    ans[0], ans[1] = 0, 0

    for i in range(2, n + 1):
        if ans[i] == 0:
            continue

        for j in range(i * i, n + 1, i):
            ans[j] = 0

    return ans


def count_prime(n: int) -> int:
    # time complexity is O(n log log n)
    # space complexity is O(n)

    # another approach is to check every number for prime
    # O(n sqrt(n)) time complexity and O(1) space complexity
    return sum(sieve(n))


if __name__ == '__main__':
    n = int(input())
    print(count_prime(n))
