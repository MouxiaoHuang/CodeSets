class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def get_top(self):
        return self.stack[-1]
        

class Queue(object):
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)
    
    def pop(self):
        self.queue.pop(0)
