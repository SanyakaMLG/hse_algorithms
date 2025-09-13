def is_palindrome(num: int) -> bool:
    # there are n operations to find num of digits in num and n / 2 operations to check if num is palindrome
    # so time complexity is O(n) and space complexity is O(1)
    if num < 0:
        raise ValueError("Parameter 'num' must be a positive integer")

    num_digits = 0
    tmp_num = num
    while tmp_num != 0:
        num_digits += 1
        tmp_num //= 10

    while num != 0:
        if num % 10 != num // 10 ** (num_digits - 1):
            return False

        num = (num % 10 ** (num_digits - 1)) // 10
        num_digits -= 2

    return True


if __name__ == '__main__':
    num = int(input())
    print(is_palindrome(num))
