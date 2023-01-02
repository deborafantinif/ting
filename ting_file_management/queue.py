class Queue:
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def search(self, index):
        n_elements = len(self.queue) - 1
        if index > n_elements or index < 0:
            raise IndexError('list index out of range')
        return self.queue[index]
