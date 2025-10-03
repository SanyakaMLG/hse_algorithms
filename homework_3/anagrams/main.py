from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for s in strs:
        groups[''.join(sorted(s))].append(s)

    res = []
    for k, v in groups.items():
        res.append(v)

    return res
