import heapq

class MinMaxHeap(object):
    def __init__(self):
        self.lowers = []
        self.highers = []

    def insert(self, item):
        if self.lowers == [] or item < -self.lowers[0]:
            heapq.heappush(self.lowers, -item)
        else:
            heapq.heappush(self.highers, item)
        self.rebalance()

    def rebalance(self):
        lowers_len = len(self.lowers)
        highers_len = len(self.highers)
        if lowers_len - highers_len > 1:
            temp = -heapq.heappop(self.lowers)
            heapq.heappush(self.highers, temp)
        elif highers_len - lowers_len > 1:
            temp = -heapq.heappop(self.highers)
            heapq.heappush(self.lowers, temp)

    def median(self):
        lowers_len = len(self.lowers)
        highers_len = len(self.highers)
        if lowers_len > highers_len:
            result = -self.lowers[0]
        elif highers_len > lowers_len:
            result = self.highers[0]
        else:
            result = float(-self.lowers[0] + self.highers[0]) / 2
        return '{:.1f}'.format(result)


if __name__ == '__main__':
    t = int(input())
    mt = MinMaxHeap()
    for _ in range(t):
        mt.insert(int(input()))
        print(mt.median())
