# https://leetcode.com/problems/lru-cache/

# Here is Solution with OrderedDict, below after that solution without OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# Here is Solution without OrderedDict, but OrderedDict also uses a Double linked list
class Node:
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


def pop_from_list(node: Node) -> Node:
    prev_node, next_node = node.prev, node.next
    if prev_node:
        prev_node.next = next_node
    if next_node:
        next_node.prev = prev_node
    return node


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.least = Node(0, 0)
        self.most = Node(0,0)
        self.least.next = self.most
        self.most.prev = self.least

    def update_mru(self, node: Node) -> None:
        prev = self.most.prev
        prev.next = node
        node.prev = prev
        node.next = self.most
        self.most.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        pop_from_list(self.cache[key])
        self.update_mru(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            pop_from_list(self.cache[key])
        self.cache[key] = Node(key, value)
        self.update_mru(self.cache[key])
        if len(self.cache) > self.capacity:
            least = self.least.next
            pop_from_list(least)
            self.cache.pop(least.key)

