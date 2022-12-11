from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()


    def enqueque(self, value):
        self.items.appendleft(value)

    def deque(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.is_empty)==0

    def size(self):
        return len(self.items)


pq = Queue()

pq.enqueque({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueque({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueque({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})


print(pq.size())
print(pq.deque())
print(pq.deque())