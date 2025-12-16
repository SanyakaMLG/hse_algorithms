def find_substring(text: str, pattern: str, P: int = 37) -> int:
    """
    Поиск подстроки в тексте, возвращает индекс первого вхождения подстроки в строку.
    Возвращает -1, если подстрока не найдена.
    """
    n = len(text)
    m = len(pattern)

    if m == 0:
        return 0
    if m > n:
        return -1

    pattern_hash = 0
    text_hash = 0

    pm = P ** (len(pattern) - 1)

    for i in range(len(pattern)):
        pattern_hash = pattern_hash * P + ord(pattern[i])
        text_hash = text_hash * P + ord(text[i])

    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i + len(pattern)]:
                return i
        
        if i + len(pattern) < len(text):
            text_hash = (text_hash - ord(text[i]) * pm) * P + ord(text[i + len(pattern)])

    return -1
