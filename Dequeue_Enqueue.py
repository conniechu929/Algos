class Queue(object):
    def __init__(self, queue=None):
        if queue is None:
            self.queue = []
        else:
            self.queue = list(queue)
    def dequeue(self):
        return self.queue.pop(0)
    def enqueue(self, element):
        self.queue.append(element)


class Queue:
    def __init__(self,queue):
        self.queue = []
    def dequeue(self):
        return self.queue.pop(0)
    def enqueue(self,element):
        self.queue.append(element)
