import pytest
import time
from hash_table.hash_table import HashTable


class TestHashTableFunctional:
    def test_basic_insert_get(self):
        ht = HashTable()
        ht["a"] = 1
        ht["b"] = 2
        assert ht["a"] == 1
        assert ht["b"] == 2

    def test_update_existing_key(self):
        ht = HashTable()
        ht["a"] = 1
        ht["a"] = 10
        assert ht["a"] == 10

    def test_key_error_on_missing_key(self):
        ht = HashTable()
        with pytest.raises(KeyError):
            _ = ht["missing"]

    def test_contains(self):
        ht = HashTable()
        ht["x"] = 42
        assert "x" in ht
        assert "y" not in ht

    def test_delete(self):
        ht = HashTable()
        ht["key"] = 100
        assert "key" in ht
        del ht["key"]
        assert "key" not in ht
        with pytest.raises(KeyError):
            del ht["key"]

    def test_len(self):
        ht = HashTable()
        assert len(ht) == 0
        ht["a"] = 1
        ht["b"] = 2
        assert len(ht) == 2
        ht["a"] = 10
        assert len(ht) == 2
        del ht["a"]
        assert len(ht) == 1

    def test_get_with_default(self):
        ht = HashTable()
        assert ht.get("missing") is None
        assert ht.get("missing", "default") == "default"

    def test_keys_values_items(self):
        ht = HashTable()
        ht["a"] = 1
        ht["b"] = 2
        ht["c"] = 3

        keys = set(ht.keys())
        values = set(ht.values())
        items = set(ht.items())

        assert keys == {"a", "b", "c"}
        assert values == {1, 2, 3}
        assert items == {("a", 1), ("b", 2), ("c", 3)}

    def test_resize_works(self):
        ht = HashTable(init_capacity=2)
        ht["a"] = 1
        ht["b"] = 2
        ht["c"] = 3
        assert ht["a"] == 1
        assert ht["b"] == 2
        assert ht["c"] == 3
        assert len(ht) == 3


class TestHashTablePerformance:
    @pytest.mark.parametrize("n", [1000, 5000, 10000, 100000, 1000000])
    def test_average_time_complexity_O1(self, n):
        ht = HashTable()

        start = time.perf_counter()
        for i in range(n):
            ht[f"key_{i}"] = i
        insert_time = time.perf_counter() - start

        start = time.perf_counter()
        for i in range(n):
            _ = ht[f"key_{i}"]
        read_time = time.perf_counter() - start

        start = time.perf_counter()
        for i in range(n):
            del ht[f"key_{i}"]
        delete_time = time.perf_counter() - start

        avg_insert = insert_time / n
        avg_read = read_time / n
        avg_delete = delete_time / n

        assert avg_insert < 0.001, f"Insert too slow: {avg_insert:.6f}s per op"
        assert avg_read < 0.001, f"Read too slow: {avg_read:.6f}s per op"
        assert avg_delete < 0.001, f"Delete too slow: {avg_delete:.6f}s per op"

    def test_constant_time_independent_of_size(self):
        sizes = [100, 1000, 10000, 50000, 100000, 1000000]
        read_times = []
        write_times = []
        del_times = []

        for n in sizes:
            ht = HashTable()
            for i in range(n):
                ht[i] = i

            start = time.perf_counter()
            _ = ht[n // 2]
            read_time = time.perf_counter() - start
            read_times.append(read_time)

            start = time.perf_counter()
            ht[n] = n
            write_time = time.perf_counter() - start
            write_times.append(write_time)

            start = time.perf_counter()
            del ht[n]
            del_time = time.perf_counter() - start
            del_times.append(del_time)

        max_time_read = max(read_times)
        min_time_read = min(read_times)

        max_time_write = max(write_times)
        min_time_write = min(write_times)

        max_time_del = max(del_times)
        min_time_del = min(del_times)
        
        assert max_time_read / min_time_read < 10, f"Read time varies too much: {read_times}"
        assert max_time_write / min_time_write < 10, f"Write time varies too much: {write_times}"
        assert max_time_del / min_time_del < 10, f"Delete time varies too much: {del_times}"