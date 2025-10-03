def two_sum(arr: list[int], target: int) -> tuple[int, int] | None:
    d = {}
    for idx, el in enumerate(arr):
        if target - el in d:
            return d[target - el], idx
        d[el] = idx

    return None
