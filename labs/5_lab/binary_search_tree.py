from queue import *
class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): #returns True if tree is empty, else False
        return self.root==None

    def search(self, key): # returns True if key is in a node of the tree, else False
       return get_key(self.root,key)
	    
    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # Example creation of node: temp = TreeNode(key, data)
        if self.root==None:
        	self.root=TreeNode(key,data)
        else:
            put_key(self.root,key,data)

    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.root==None:
            return None
        return get_min(self.root)

    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
       	if self.root==None:
            return None
        return get_max(self.root)

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.root==None:
            return None
        return get_height([self.root], -1)

    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        if self.root==None:
            return []
        return get_inorder(self.root)

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        if self.root==None:
            return []
        return get_preorder(self.root)	

    def postorder(self):
        if self.root==None:
            return []
        return get_postorder(self.root)

    def delete(self, key): # deletes node containing key
        # Will need to consider all cases 
        # This is the most difficult method - save it for last, so that
        # if you cannot get it to work, you can still get credit for 
        # the other methods
        # Returns True if the item was deleted, False otherwise
        temp, parent, path = get_parent(self.root,self.root,key,'root')
        if path==None:
            return False
        if temp.left==None and temp.right==None:
            if path=='left':
                parent.left=None
            elif path=='right':
                parent.right=None
            else:
                self.root=None
        elif temp.right==None:
            if path=='left':
                parent.left, parent.left.data = temp.left, temp.left.data
            elif path=='right':
                parent.right, parent.right.data = temp.left, temp.left.data
            else:
                self.root, self.root.data = temp.left, temp.left.data
        elif temp.left==None:
            if path=='left':
                parent.left, parent.left.data = temp.right, temp.right.data
            elif path=='right':
                parent.right, parent.right.data = temp.right, temp.right.data
            else: 
                self.root, self.root.data = temp.right, temp.right.data
        else:
            target=temp
            if path=='left':
                temp=temp.left
                while temp.right!=None:
                    target, temp = temp, temp.right
            else:
                temp=temp.right
                while temp.left!=None:
                    target, temp = temp, temp.left
            if path=='left':
                parent.left.key, parent.left.data = temp.key, temp.data
            elif path=='right':
                parent.right.key, parent.right.data = temp.key, temp.data
            else:
                self.root.key, self.root.data = temp.key, temp.data
            if target.left!=None and target.left.key==temp.key:
                if temp.left!=None:
                    target.left, target.left.data = temp.left, temp.left.data
                else:
                    target.left=temp.right
            else:
                if temp.right!=None:
                    target.right, target.right.data = temp.right, temp.right.data
                else:
                   target.right=temp.left
        return True

    def levelorder(self):
        nums=[]
        roots=Queue(self.tree_height() ** 2 + 2)
        roots.enqueue(self.root)
        while roots.num_items!=0:
            root=roots.dequeue()
            nums.append(root.key)
            if root.left!=None and root.right!=None:
                roots.enqueue(root.left)
                roots.enqueue(root.right)
            elif root.left!=None:
                roots.enqueue(root.left)
            elif root.right!=None:
                roots.enqueue(root.right)
        return nums

    def changeTreeRoot(self,key):
        if self.root.key==key:
            pass
        elif self.delete(key):
            new=BinarySearchTree()
            new.insert(key)
            for i in self.preorder_list():
                new.insert(i)
            self.root=new.root

def get_parent(root,parent,key,path):
    if root==None:
        return None, None, None
    if root.key==key:
        return root, parent, path
    if root.key<key:
        return get_parent(root.right,root,key,'right')
    return get_parent(root.left,root,key,'left')

def put_key(root,key,data):
    if root.key<key:
        if root.right==None:
            root.right=TreeNode(key,data)
        return put_key(root.right,key,data)
    if key<root.key:
        if root.left==None:
            root.left=TreeNode(key,data)
        return put_key(root.left,key,data)
    root.data=data

def get_preorder(root):
	if root.left!=None and root.right!=None:
		return [root.key]+get_preorder(root.left)+get_preorder(root.right)
	if root.left!=None:
		return [root.key]+get_preorder(root.left)
	if root.right!=None:
		return [root.key]+get_preorder(root.right)
	return [root.key]

def get_inorder(root):
	if root.left!=None and root.right!=None:
		return get_inorder(root.left)+[root.key]+get_inorder(root.right)
	if root.left!=None:
		return get_inorder(root.left)+[root.key]
	if root.right!=None:
		return [root.key]+get_inorder(root.right)
	return [root.key]

def get_postorder(root):
    if root.left!=None and root.right!=None:
        return get_postorder(root.left)+get_postorder(root.right)+[root.key]
    if root.left!=None:
        return get_postorder(root.left)+[root.key]
    if root.right!=None:
        return get_postorder(root.right)+[root.key]
    return [root.key]

def get_height(branches,count):
    if len(branches)==0:
        return count
    new=[]
    for i in branches: 
        if i.left!=None:
            new.append(i.left)
        if i.right!=None:
            new.append(i.right)
    return get_height(new,count+1)

def get_key(root,key):
    if root==None:
        return False
    if root.key==key:
        return True
    if root.key<key:
        return get_key(root.right,key)
    return get_key(root.left,key)

def get_min(root):
    if root.left==None:
        return (root.key,root.data)
    return get_min(root.left)
    
def get_max(root):
    if root.right==None:
        return (root.key,root.data)
    return get_max(root.right)
