import random
import time

def selection_sort(list):
    comps=0
    for i in range(len(list)):
        n=m=i
        for ii in range(i+1,len(list)):
            if list[ii]<list[m]:
                m=ii
            comps+=1
        list[n],list[m]=list[m],list[n]
    return comps
     
def insertion_sort(list):
    comps=0
    for i in range(1,len(list)):
        ii=i-1
        while list[i]<list[ii]:
            n=ii
            comps+=1
            if n==0:
                break
            ii-=1
        try:
            list.insert(n,list.pop(i))
            del n
            comps+=1
        except UnboundLocalError:
            comps+=1
    return comps 

def merge_sort(vaules):
    if len(vaules)>1:
        m=len(vaules)//2
        left=vaules[:m]
        right=vaules[m:]
        left = merge_sort(left)
        right = merge_sort(right)

        vaules = []
        while len(left)>0 and len(right)>0:
            if left[0]<right[0]:
                vaules.append(left[0])
                left.pop(0)
            else:
                vaules.append(right[0])
                vaules.pop(0)
        for i in left:
            vaules.append(i)
        for i in right:
            vaules.append(i)
    return vaules

def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 8000)
    randoms2 = list(randoms)
#    start_time = time.time() 
 #   comps = selection_sort(randoms)
  #  stop_time = time.time()
   # print(comps, stop_time - start_time)
    start_time = time.time() 
    comps = insertion_sort(randoms2)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

