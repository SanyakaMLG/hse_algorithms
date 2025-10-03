import time
import matplotlib.pyplot as plt
from hash_table import HashTable

def benchmark_hash_table():
    sizes = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 250000, 500000, 1000000, 2000000]
    insert_times = []
    read_times = []
    delete_times = []

    insert_times_avg = []
    read_times_avg = []
    delete_times_avg = []
    
    for n in sizes:
        print(f"Benchmarking size: {n}")

        ht = HashTable()
        start = time.perf_counter()
        for i in range(n):
            ht[f"key_{i}"] = i
        total_insert = time.perf_counter() - start
        avg_insert = total_insert / n
        insert_times.append(total_insert)
        insert_times_avg.append(avg_insert)

        start = time.perf_counter()
        for i in range(n):
            _ = ht[f"key_{i}"]
        total_read = time.perf_counter() - start
        avg_read = total_read / n
        read_times.append(total_read)
        read_times_avg.append(avg_read)

        start = time.perf_counter()
        for i in range(n):
            del ht[f"key_{i}"]
        total_delete = time.perf_counter() - start
        avg_delete = total_delete / n
        delete_times.append(total_delete)
        delete_times_avg.append(avg_delete)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, insert_times, label='Insert total time', marker='o')
    plt.plot(sizes, read_times, label='Read total time', marker='s')
    plt.plot(sizes, delete_times, label='Delete total time', marker='^')

    plt.xlabel('Number of operations (n)')
    plt.ylabel('Total time (seconds)')
    plt.title('HashTable Performance: Total Time vs. Number of Operations')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.savefig('hash_table_total_time.png', dpi=150, bbox_inches='tight')
    print("График 1 сохранён как 'hash_table_total_time.png'")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, insert_times_avg, label='Insert (avg per op)', marker='o')
    plt.plot(sizes, read_times_avg, label='Read (avg per op)', marker='s')
    plt.plot(sizes, delete_times_avg, label='Delete (avg per op)', marker='^')

    plt.xlabel('Number of elements (n)')
    plt.ylabel('Average time per operation (seconds)')
    plt.title('HashTable Performance: Average Time per Operation vs. Data Size')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.yscale('log')

    plt.savefig('hash_table_performance.png', dpi=150, bbox_inches='tight')
    print("График 2 сохранён как 'hash_table_performance.png'")

if __name__ == "__main__":
    benchmark_hash_table()