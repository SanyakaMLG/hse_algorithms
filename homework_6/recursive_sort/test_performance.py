import pytest
import random
from recursive_sort.quicksort import quicksort, quicksort_inplace
from recursive_sort.mergesort import mergesort
import sys

sys.setrecursionlimit(10_000)

N = 2000

# run pytest -s recursive_sort/test_performance.py for check exact difference
def print_result(name, t1, t2):
    print(f"{name}: {t1:.5f} сек vs {t2:.5f} сек (разница: {abs(t1-t2):.5f} сек, в {t1/t2:.2f} раз)")

def test_sorted_vs_reversed():
    arr_sorted = list(range(N))
    arr_reversed = list(range(N, 0, -1))

    # mergesort всегда O(n log n)
    _, t_merge_sorted = mergesort(arr_sorted)
    _, t_merge_reversed = mergesort(arr_reversed)

    # quicksort выбор среднего элемента
    # худший случай - лесенка в середине массива в обе стороны (либо гора либо впадина ∧ V)
    _, t_quick_sorted = quicksort(arr_sorted)
    _, t_quick_reversed = quicksort(arr_reversed)

    # quicksort_inplace выбор последнего элемента, на отсортированном и обратном массиве — худший случай
    arr1 = arr_sorted[:]
    arr2 = arr_reversed[:]
    _, t_quick_inplace_sorted = quicksort_inplace(arr1)
    _, t_quick_inplace_reversed = quicksort_inplace(arr2)

    print_result("quicksort_inplace (sorted)/mergesort (sorted)", t_quick_inplace_sorted, t_merge_sorted)
    print_result("quicksort_inplace (reversed)/mergesort (reversed)", t_quick_inplace_reversed, t_merge_reversed)
    print_result("quicksort_inplace (sorted)/quicksort (sorted)", t_quick_inplace_sorted, t_quick_sorted)
    print_result("quicksort_inplace (reversed)/quicksort (reversed)", t_quick_inplace_reversed, t_quick_reversed)

    assert t_quick_inplace_sorted > t_merge_sorted * 3
    assert t_quick_inplace_reversed > t_merge_reversed * 3

def test_many_duplicates():
    arr = [5] * N

    _, t_merge = mergesort(arr)
    _, t_quick = quicksort(arr)
    arr2 = arr[:]
    _, t_quick_inplace = quicksort_inplace(arr2)

    print_result("quicksort/mergesort (many duplicates)", t_quick, t_merge)
    print_result("quicksort_inplace/mergesort (many duplicates)", t_quick_inplace, t_merge)
    print_result("quicksort_inplace/quicksort (many duplicates)", t_quick_inplace, t_quick)
    assert t_quick_inplace > t_merge * 1.5

def test_random_large():
    arr = [random.randint(0, 10_000) for _ in range(N)]

    arr1 = arr[:]
    arr2 = arr[:]
    arr3 = arr[:]

    _, t_quick = quicksort(arr1)
    _, t_quick_inplace = quicksort_inplace(arr2)
    _, t_merge = mergesort(arr3)

    print_result("quicksort/quicksort_inplace (random)", t_quick, t_quick_inplace)
    print_result("quicksort/mergesort (random)", t_quick, t_merge)
    print_result("quicksort_inplace/mergesort (random)", t_quick_inplace, t_merge)
    assert t_quick_inplace < t_quick * 1.2

def test_almost_sorted():
    arr = list(range(N))
    arr[N//2], arr[N//2+1] = arr[N//2+1], arr[N//2]  # swap two elements

    _, t_merge = mergesort(arr)
    _, t_quick = quicksort(arr)
    arr2 = arr[:]
    _, t_quick_inplace = quicksort_inplace(arr2)

    print_result("quicksort_inplace/mergesort (almost sorted)", t_quick_inplace, t_merge)
    print_result("quicksort/mergesort (almost sorted)", t_quick, t_merge)
    print_result("quicksort_inplace/quicksort (almost sorted)", t_quick_inplace, t_quick)
    assert t_quick_inplace > t_merge * 2
