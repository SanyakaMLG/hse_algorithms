import time
import random
from main import makeheap_n_log_n, makeheap
import matplotlib.pyplot as plt

def compare_time():
    size_repeats = {
        1000: 100,
        10000: 50,
        100000: 10,
        1000000: 3,
        10000000: 2,
    }

    sizes = list(size_repeats.keys())
    repeat_counts = list(size_repeats.values())
    n_log_n_times = []
    n_times = []

    for size, repeats in zip(sizes, repeat_counts):
        n_log_n_total = 0
        n_total = 0

        for _ in range(repeats):
            arr = [random.randint(0, 1000000) for _ in range(size)]

            start = time.time()
            makeheap_n_log_n(arr.copy())
            end = time.time()
            n_log_n_total += end - start

            start = time.time()
            makeheap(arr.copy())
            end = time.time()
            n_total += end - start

        avg_n_log_n = n_log_n_total / repeats
        avg_n = n_total / repeats
        n_log_n_times.append(avg_n_log_n)
        n_times.append(avg_n)

        print(f"Size: {size}, Repeats: {repeats}, Avg makeheap_n_log_n: {avg_n_log_n:.5f}s, Avg makeheap: {avg_n:.5f}s")

    plot_results(sizes, n_log_n_times, n_times)


def plot_results(sizes, n_log_n_times, n_times):
    plt.figure(figsize=(12, 7))

    plt.plot(sizes, n_log_n_times, label='makeheap_n_log_n (O(n log n))', marker='o', linestyle='-', linewidth=2)
    plt.plot(sizes, n_times, label='makeheap (O(n))', marker='s', linestyle='-', linewidth=2)

    plt.xscale('log')
    plt.yscale('linear')

    min_time = min(min(n_log_n_times), min(n_times))
    max_time = max(max(n_log_n_times), max(n_times))
    plt.ylim(min_time * 0.9, max_time * 1.1)

    for i, (size, n_log_n, n) in enumerate(zip(sizes, n_log_n_times, n_times)):
        diff_ms = (n_log_n - n) * 1000
        plt.annotate(f'{diff_ms:.2f} ms',
                     (size, (n_log_n + n) / 2),
                     textcoords="offset points",
                     xytext=(0, 10),
                     ha='center',
                     fontsize=9,
                     color='black')

    plt.xlabel('Размер массива (log шкала)')
    plt.ylabel('Среднее время выполнения (секунды)')
    plt.title('Сравнение времени выполнения алгоритмов построения кучи')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()

    plt.savefig('heap_comparison_avg_zoomed.png')
    plt.close()


compare_time()
