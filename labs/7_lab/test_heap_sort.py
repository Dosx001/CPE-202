from heap import *
from random import randrange as rand

def main():
    if input("Test? ")=="sort":
        for i in range(int(input("Num of runs? "))):
            alist, other, copy = sort_test()
            if alist!=None:
                print('Failed')
                print('List:',alist)
                print('Sort:',other)
                print('Copy:',copy)
                break
            print(f'Good run #{i}')
            print('-'*40)
    for i in range(int(input("Num of runs? "))):
        alist, num1, num2 = enqueue_test()
        if alist!=None:
            print('Failed')
            print('List:',alist)
            print('nums:',num1,num2)
            break
        print(f'Good run #{i}')
        print('-'*40)
    
def sort_test():
    alist=[rand(-99,99) for i in range(rand(10))]
    copy=list(alist)
    copy.sort()
    heap_tree=MaxHeap()
    other=list(alist)
    if heap_tree.heap_sort_ascending(other)==copy:
        return None, None, None
    else:
        return alist, other, copy 
  
def enqueue_test():
    alist=[rand(-99,99) for i in range(rand(3,10))]
    num1=rand(-99,99)
    num2=rand(-99,99)
    
    copy=list(alist)
    copy.remove(max(copy))
    try:
        copy.remove(max(copy))
    except ValueError:
        print('afsd')
        print(copy)
        print(max(copy))
    copy.append(num1)
    copy.append(num2)
    copy.sort()
    
    heap_tree=MaxHeap()
    heap_tree.build_heap(list(alist))
    heap_tree.dequeue()
    heap_tree.dequeue()
    try:
        heap_tree.enqueue(num1)
        heap_tree.enqueue(num2)
    except TypeError:
        print("Enqueue Error")
        return alist, num1, num2
    nums=[heap_tree.dequeue() for i in range(heap_tree.size)]
    #try:
     #   nums.sort()
    #except TypeError:
     #   print("Sorting Error")
      #  print("copy:",copy)
       # return alist, num1, num2
    if nums[::-1]==copy:
        return None, None, None
    print(nums[::-1])
    return alist, num1, num2

if __name__=="__main__":
    main() 
