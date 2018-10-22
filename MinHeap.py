class MinHeap:
    def __init__(self, data=[]):
        self.data = data
        heapq.heapify(data)

    def insert(self, num):
        heapq.heappush(self.data, num)

    def getMin(self):
        if not self.data:
            return None
        else:
            return self.data[0]

    def extractMin(self):
        if not self.data:
            raise IndexError("Heap is Empty")
        else:
            return heapq.heappop(self.data)

    def eleCount(self):
        return len(self.data)
