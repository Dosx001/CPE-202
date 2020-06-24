class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.items = [None] * capacity
        self.num_items = self.front = self.rear = 0

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        return self.num_items == 0

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        return self.capacity == self.num_items

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if self.capacity == self.num_items:
            raise IndexError
        self.items[self.rear] = item
        if self.rear != self.capacity - 1:
            self.rear += 1
        else:
            self.rear = 0
        self.num_items += 1

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if self.num_items == 0:
            raise IndexError
        x = self.items[self.front]
        # self.items[self.front] = None
        if self.front != self.capacity-1:
            self.front += 1
        else:
            self.front = 0
        self.num_items -= 1
        return x

    def peek(self):
        if self.num_items == 0:
            raise IndexError
        return self.items[self.front]

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items
