import heapq

class MaxHeap:
    def __init__(self,data = []):
        self.data = [i*-1 for i in data]
        heapq.heapify(data)

    def insert(self, num):
        num = num*-1
        heapq.heappush(self.data, num)

    def getMax(self):
        if not self.data:
            return None
        else:
            return self.data[0]*-1

    def extractMax(self):
        if not self.data:
            raise IndexError("Heap is Empty")
        else:
            return heapq.heappop(self.data)*-1

    def eleCount(self):
        return len(self.data)
