class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class HashTable:
    def __init__(self, init_capacity: int = 8):
        if init_capacity < 1:
            raise ValueError("Initial capacity must be at least 1")
            
        self._capacity = init_capacity
        self._load_factor = 0.75
        self._size = 0
        self._buckets = [Node(None) for _ in range(self._capacity)]

    def _hash(self, key):
        return hash(key) % self._capacity

    def _resize(self):
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [Node(None) for _ in range(self._capacity)]
        self._size = 0

        for bucket in old_buckets:
            ptr = bucket.next
            while ptr:
                self[ptr.val[0]] = ptr.val[1]
                ptr = ptr.next

    def __setitem__(self, key, value):
        if self._size >= self._capacity * self._load_factor:
            self._resize()

        idx = self._hash(key)
        pair = (key, value)
        prev = self._buckets[idx]
        cur = prev.next

        while cur:
            if cur.val[0] == key:
                cur.val = pair
                return
            prev = cur
            cur = cur.next

        node = Node(pair)
        prev.next = node
        self._size += 1

    def __getitem__(self, key):
        idx = self._hash(key)
        cur = self._buckets[idx].next
        while cur:
            if cur.val[0] == key:
                return cur.val[1]
            cur = cur.next

        raise KeyError(key)

    def __delitem__(self, key):
        idx = self._hash(key)
        prev = self._buckets[idx]
        cur = prev.next

        while cur:
            if cur.val[0] == key:
                prev.next = cur.next
                del cur
                self._size -= 1
                return
            prev = prev.next
            cur = cur.next

        raise KeyError(key)

    def __len__(self):
        return self._size

    def __contains__(self, key):
        idx = self._hash(key)
        cur = self._buckets[idx].next
        while cur:
            if cur.val[0] == key:
                return True
            cur = cur.next

        return False

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def keys(self):
        res = []
        for ptr in self._buckets:
            tmp_ptr = ptr.next
            while tmp_ptr:
                res.append(tmp_ptr.val[0])
                tmp_ptr = tmp_ptr.next

        return res

    def values(self):
        res = []
        for ptr in self._buckets:
            tmp_ptr = ptr.next
            while tmp_ptr:
                res.append(tmp_ptr.val[1])
                tmp_ptr = tmp_ptr.next

        return res

    def items(self):
        res = []
        for ptr in self._buckets:
            tmp_ptr = ptr.next
            while tmp_ptr:
                res.append(tmp_ptr.val)
                tmp_ptr = tmp_ptr.next

        return res
        