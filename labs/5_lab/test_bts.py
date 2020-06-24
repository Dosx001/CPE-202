from binary_search_tree import *
from random import randrange as rand, shuffle as shf

def main():
    for i in range(int(input('Number of Runs? '))):
        nums,shake=test()
        if nums!=None:
            print(nums)
            print(shake)
            break
        print(f'Run #{i}')
        print('-'*40)

def test():
    nums=set(rand(100000) for i in range(rand(1,30)))
    shake=list(nums)
    bst=BinarySearchTree()
    n=0
    while bst.is_empty():
        for i in nums:
            bst.insert(i,i)
        try:
            bst.levelorder()
        except IndexError:
            print('IndexError')
            return nums, None
        shf(shake)
        for i in shake:
            if bst.root.key!=bst.root.data:
                print(f'Data Error: {bst.root.key}!={bst.root.data} on {i}')
                return nums,shake
            if not bst.delete(i):
                print(f'Deletion Error: {i} not found')
                return nums,shake
        n+=1
        if n==10:
            print('Good Run')
            return None, None

if __name__=='__main__':
    main()
