def even_sum(nums: list[int]) -> int:
    # time complexity is O(n) for find min even num in list and get sum of elements
    # space complexity is O(1)
    min_odd = None
    s = 0
    for i, num in enumerate(nums):
        if num % 2 == 1 and (min_odd is None or num < min_odd):
            min_odd = num
        s += num

    if min_odd is None or s % 2 == 0:
        return s

    return s - min_odd


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(even_sum(nums))
