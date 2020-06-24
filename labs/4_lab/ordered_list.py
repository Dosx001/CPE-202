class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    def __init__(self):
        self.items=Node(None)

    def is_empty(self):
        return self.items.next==None

    def add(self, item):
        if self.items.next==None:
            self.items.next = self.items.prev = Node(item)
            self.items.next.next = self.items.prev.prev = self.items
        else:
            temp=self.items
            while temp.next.item<item:
                temp=temp.next
                if temp.next.item==None:
                    break
            if temp.next.item!=item:
                temp.next.prev=Node(item)
                temp.next.prev.next=temp.next
                temp.next.prev.prev=temp
                temp.next=temp.next.prev

    def remove(self,item):
        if self.items.next==None:
            return False
        temp=self.items.next
        while True:
            if temp.item==item:
                temp.prev.next=temp.next
                temp.next.prev=temp.prev
                if self.items.next==self.items:
                    self.items=Node(None)
                return True
            if temp.item==None:
                return False
            temp=temp.next

    def index(self,item):
        if self.items.next==None:
            return None
        index=0
        temp = self.items.next
        while temp.item!=None:
            if temp.item==item:
                return index
            index+=1
            temp=temp.next
        return None

    def pop(self,index):
        if index<=-1 or self.items.next==None:
            raise IndexError
        temp=self.items.next
        for i in range(index):
            temp=temp.next
            if temp.item==None:
                raise IndexError
        item=temp.item
        temp.prev.next=temp.next
        temp.next.prev=temp.prev
        if self.items.next==self.items:
            self.items=Node(None)
        return item

    def search(self,item):
        if self.items.next==None:
            return False
        def finder(x,item):
            if x.item==item:
                return True
            if x.item==None:
                return False
            return finder(x.next,item)
        return finder(self.items.next,item)

    def python_list(self):
        if self.items.next==None:
            return []
        list=[]
        temp=self.items.next
        while temp.item!=None:
            list.append(temp.item)
            temp=temp.next
        return list

    def python_list_reversed(self):
        if self.items.next==None:
            return []
        def faller(x):
            if x.next.item==None:
                return [x.item]
            return faller(x.next)+[x.item]
        return faller(self.items.next)

    def size(self):
        if self.items.next==None:
            return 0
        def counter(x):
            if x.next.item==None:
                return 1
            return counter(x.next)+1
        return counter(self.items.next)
