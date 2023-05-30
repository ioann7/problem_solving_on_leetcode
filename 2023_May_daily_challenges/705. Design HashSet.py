# https://leetcode.com/problems/design-hashset/

class MyHashSet:

    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.data = [list() for _ in range(self.capacity)]

    def add(self, key: int) -> None:
        if self.size == self.capacity:
            self._update_capacity()
        if not self.contains(key):
            self.data[key % self.capacity].append(key)
            self.size += 1

    def remove(self, key: int) -> None:
        for index, value in enumerate(self.data[key % self.capacity]):
            if value == key:
                self.data[key % self.capacity][index] = self.data[key % self.capacity][-1]
                self.data[key % self.capacity].pop()
                self.size -= 1
                break

    def contains(self, key: int) -> bool:
        if key in self.data[key % self.capacity]:
            return True
        return False

    def _update_capacity(self) -> None:
        self.capacity *= 2
        temp = self.data
        self.data = [list() for _ in range(self.capacity)]
        for keys in temp:
            for key in keys:
                self.add(key)
