class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, n):
        self.heap.append(n)
        temp_index = len(self.heap) - 1
        while (temp_index - 1)//2 >= 0:
            parent_index = (temp_index - 1)//2
            if self.heap[parent_index] > self.heap[temp_index]:
                self.heap[parent_index], self.heap[temp_index] = self.heap[temp_index], self.heap[parent_index]
                temp_index = parent_index
            else:
                break

    def delete(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        q = self.heap.pop()
        if len(self.heap) > 1:
            temp_index_0 = 0
            while 2*temp_index_0 + 1 < len(self.heap):
                child_index = 2 * temp_index_0 + 1
                if 2 * temp_index_0 + 2 < len(self.heap):
                    if self.heap[2 * temp_index_0 + 1] > self.heap[2 * temp_index_0 + 2]:
                        child_index = 2 * temp_index_0 + 2

                if self.heap[temp_index_0] > self.heap[child_index]:
                    self.heap[temp_index_0], self.heap[child_index] = self.heap[child_index], self.heap[temp_index_0]
                    temp_index_0 = child_index
                else:
                    break
        return q


def main():
    n = int(input())
    heap = BinaryHeap()
    for i in range(n):
        os = [int(x) for x in input().split()]
        if os[0] == 1:
            heap.insert(os[1])
        else:
            print(heap.delete())


if __name__ == '__main__':
    main()
