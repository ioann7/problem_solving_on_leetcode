# https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet:

    def __init__(self):
        self.hash_map = {}   # value: index of array
        self.array = []

    def insert(self, val: int) -> bool:
        if val not in self.hash_map:
            self.hash_map[val] = len(self.array)
            self.array.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hash_map:
            index = self.hash_map[val]
            self.array[index] = self.array[-1]
            self.hash_map[self.array[index]] = index
            self.array.pop()
            self.hash_map.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.array)
