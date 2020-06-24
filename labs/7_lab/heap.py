class MaxHeap:
    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50
        but allows heaps of other capacities to be created."""
        self.cap=capacity
        self.size = 0
        self.heap = [None]*(capacity+1) 
        
    def enqueue(self, item):
        """inserts "item" into the heap, returns true if successful, 
        false if there is no room in the heap"""
        if self.size==self.cap:
            return False
        self.size+=1
        if self.heap[self.size]==None:
            self.heap[self.size]=item
            self.perc_up(self.size)
        else:
            n=1
            while self.heap[n]!=None:
                n+=1
            self.heap[n]=item
            self.perc_up(n)
        return True 
       
    def peek(self):
        """returns max without changing the heap, returns None if the heap is empty"""        
        if self.heap[1]==None:
            return None
        return self.heap[1]

    def dequeue(self):
        """returns max and removes it from the heap and restores the heap property
        returns None if the heap is empty"""
        if self.heap[1]==None:
            return None
        top,self.heap[1]=self.heap[1], self.heap[self.size]
        self.heap[self.size]=None
        self.perc_down(1)
        self.size-=1
        return top

    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)"""
        return self.heap[1:self.size+1]

    def build_heap(self, alist):
        """Builds a heap from the items in alist and builds a heap using the bottom up method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased"""
        if self.cap<self.size+len(alist):
            self.cap+=self.size+len(alist)-self.cap
            self.heap=[None]*(self.cap+1)
        self.size=len(alist)
        for i in range(1,len(alist)+1):
            self.heap[i]=alist[i-1]
        for i in range(len(alist)//2,0,-1):
            self.perc_down(i)

    def is_empty(self):
        """returns True if the heap is empty, false otherwise"""
        return self.size==0

    def is_full(self):
        """returns True if the heap is full, false otherwise"""
        return self.cap==self.size

    def capacity(self):
        """this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return self.cap
    
    def get_size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.size
        
    def perc_down(self, i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        l=2*i
        r=2*i+1
        while True:
            checker=[]
            if l<=self.cap and self.heap[l]!=None and self.heap[i]<self.heap[l]:
                checker.append('l')
            if r<=self.cap and self.heap[r]!=None and self.heap[i]<self.heap[r]:
                checker.append('r')
            if len(checker)==2:
                if self.heap[l]<self.heap[r]:
                    checker=['r']
                else:
                    checker=['l']
            if 'l' in checker:
                self.heap[i],self.heap[l]=self.heap[l],self.heap[i]
                i=l
                r=2*l+1
                l=2*l
            elif 'r' in checker:
                self.heap[i],self.heap[r]=self.heap[r],self.heap[i]
                i=r
                l=2*r
                r=2*r+1
            else:
                break
      
    def perc_up(self, i):
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        top=i//2
        while 0<top:
            if self.heap[top]<self.heap[i]:
                self.heap[top],self.heap[i]=self.heap[i],self.heap[top]
            i=top
            top//=2

    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order"""
        self.heap=[None]*(self.cap+1)
        self.size=0
        self.build_heap(alist)
        for i in range(len(alist)-1,-1,-1):
            alist[i]=self.dequeue()
        return alist
