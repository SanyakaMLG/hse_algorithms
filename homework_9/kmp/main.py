def compute_prefix_function(s: str) -> list[int]:
    m = len(s)
    pi = [0] * m
    j = 0
    
    for i in range(1, m):
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        
        if s[i] == s[j]:
            j += 1
        
        pi[i] = j
    
    return pi


def kmp(text: str, pattern: str) -> int:
    """
    Поиск подстроки в тексте, возвращает индекс первого вхождения подстроки в строку.
    Возвращает -1, если подстрока не найдена.
    """
    n = len(text)
    m = len(pattern)
    
    if m == 0:
        return 0

    pi = compute_prefix_function(pattern)
    
    j = 0

    for i in range(n):
        while j > 0 and pattern[j] != text[i]:
            j = pi[j-1]
        
        if pattern[j] == text[i]:
            j += 1
        
        if j == m:
            return i - m + 1
            
    return -1
