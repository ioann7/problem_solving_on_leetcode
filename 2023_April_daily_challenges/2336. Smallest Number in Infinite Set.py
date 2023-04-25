class SmallestInfiniteSet:

    def __init__(self):
        self.data = []
        self.set_data = set()
        self.current_int = 1

    def popSmallest(self) -> int:
        if self.data:
            value = heapq.heappop(self.data)
            self.set_data.discard(value)
        else:
            value = self.current_int
            self.current_int += 1
        return value

    def addBack(self, num: int) -> None:
        if num not in self.set_data and num < self.current_int:
            self.set_data.add(num)
            heapq.heappush(self.data, num)


# My first solution.
class SmallestInfiniteSet:

    def __init__(self):
        self.data = list(range(1, 1002))
        self.set_data = set(self.data)
        heapq.heapify(self.data)

    def popSmallest(self) -> int:
        value = heapq.heappop(self.data)
        self.set_data.discard(value)
        return value

    def addBack(self, num: int) -> None:
        if num not in self.set_data:
            self.set_data.add(num)
            heapq.heappush(self.data, num)
