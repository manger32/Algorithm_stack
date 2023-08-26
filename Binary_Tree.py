class TreeNode():
    # It instantiates the class
    def __init__ (self, val):
        self.val = val
        self.place = 0
        self.height = 1
        self.leftChild = None
        self.rightChild = None

# Self Balancing Binary Search Tree based on the type of AVL Trees
class sbbst():
    # It instantiates the class O(1)
    def __init__(self, valslist = None):
        self.head = None
        self.NodeCnt = 0
        self.count = 0
        self.sizes = []
        self.sumsizes = []
        self.listInOrder = []
        if type(valslist) == list:
            for val in valslist:
                self.head = self.insertNode(self.head, val)

    # It return True if the val is found, False otherwhise O(logN)
    def search(self, node, val):
        if not node:
            return False
        else:
            if node.val < val:
                return self.search(node.rightChild, val)
            elif val < node.val:
                return self.search(node.leftChild, val)
            else:
                return True

    # It inserts a node and updates the head node O(logN)
    def insert(self, val):
        self.head = self.insertNode(self.head, val)
    
    # It inserts a node with a value and returns the node of the modified subtree O(logN)
    def insertNode(self, node, key):
        # Step 1 - Perform normal BST
        if not node:
            self.NodeCnt += 1
            return TreeNode(key)
        
        elif key < node.val:
            node.leftChild = self.insertNode(node.leftChild, key)
        else:
            node.rightChild = self.insertNode(node.rightChild, key)
        
        # 2: Update the height of the node
        node.height = 1 + max(self.getHeight(node.leftChild), self.getHeight(node.rightChild))
        # 3: Get the balance factor
        balance = self.getBalance(node)
        # 4: If the node is unbalanced, try out the 2 cases
        if balance > 1: # Case 1: leftChild (leftChild/rightChild)
            if key > node.leftChild.val:
                node.leftChild = self.leftChildRotate(node.leftChild)
            return self.rightChildRotate(node)
        if balance < -1: # Case 2: rightChild (leftChild/rightChild)
            if key < node.rightChild.val:
                node.rightChild = self.rightChildRotate(node.rightChild)
            return self.leftChildRotate(node)
        # Return the result node
        return node

    # It deletes a node with a certain value and updates the head node O(logN)
    def delete(self, val):
        self.head = self.deleteNode(self.head, val)

    # It deletes a node with a certain value and returns the node of the modified subtree O(logN)
    def deleteNode(self, node, key):
        # 1: Standard BST delete
        if not node:
            return node

        elif key < node.val:
            node.leftChild = self.deleteNode(node.leftChild, key)
        elif key > node.val:
            node.rightChild = self.deleteNode(node.rightChild, key)

        else: # key == node.val            
            if node.leftChild is None:
                self.NodeCnt -= 1
                temp = node.rightChild
                node = None
                return temp
            elif node.rightChild is None:
                self.NodeCnt -= 1
                temp = node.leftChild
                node = None
                return temp
            else: # node.leftChild and node.rightChild
                temp = self.getMinValueNode(node.rightChild)
                node.val = temp.val
                node.rightChild = self.deleteNode(node.rightChild, temp.val)

        # Return None if there is no more nodes
        if node is None:
            return node
        # 2: Update the height of the node
        node.height = 1 + max(self.getHeight(node.leftChild), self.getHeight(node.rightChild))
        # 3: Get the balance factor
        balance = self.getBalance(node)
        # 4: If the node is unbalanced, try out the 2 cases
        if balance > 1: # Case 1: leftChild (leftChild/rightChild)
            if self.getBalance(node.leftChild) < 0:
                node.leftChild = self.leftChildRotate(node.leftChild)
            return self.rightChildRotate(node)
        if balance < -1:# Case 2: rightChild (rightChild/leftChild)
            if self.getBalance(node.rightChild) > 0:
                node.rightChild = self.rightChildRotate(node.rightChild)
            return self.leftChildRotate(node)
        # Return the result node
        return node 
    
    # It rotates the tree to the leftChild and returns the node O(1)
    def leftChildRotate(self, node):
        rnode = node.rightChild
        T = rnode.leftChild
        # Perform rotation
        rnode.leftChild = node
        node.rightChild = T
        # Update heights
        node.height = 1 + max(self.getHeight(node.leftChild), self.getHeight(node.rightChild))
        rnode.height = 1 + max(self.getHeight(rnode.leftChild), self.getHeight(rnode.rightChild))
        # Return the new node
        return rnode

    # It rotates the tree to the rightChild and returns the node O(1)
    def rightChildRotate(self, node):
        lnode = node.leftChild
        T = lnode.rightChild
        # Perform rotation
        lnode.rightChild = node
        node.leftChild = T
        # Update heights
        node.height = 1 + max(self.getHeight(node.leftChild), self.getHeight(node.rightChild))
        lnode.height = 1 + max(self.getHeight(lnode.leftChild), self.getHeight(lnode.rightChild))
        # Return the new node
        return lnode

    # It returns the height of a node O(1)
    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    # It returns the balance of the node O(1)
    def getBalance(self, node): 
        if not node:
            return 0
        return self.getHeight(node.leftChild) - self.getHeight(node.rightChild)

    # It returns the min Node O(logN)
    def getMinValueNode(self, node):
        if node is None or node.leftChild is None:
            return node
        return self.getMinValueNode(node.leftChild)

    # It returns the min value of the Tree O(logN + K)
    def kthsmallest(self, K):
        if K < 0:
            print('There are not enough elements in the Tree')
            return None
        elif self.NodeCnt//2+1 < K:
            return self.kthlargest(self.NodeCnt+1-K)
        else:
            stack = []
            node = self.head
            while(stack or node):
                if node:
                    stack.append(node)
                    node = node.leftChild
                else:
                    node = stack.pop()
                    if K == 1:
                        return node.val
                    else:
                        K -= 1
                    node = node.rightChild
    
    # It returns the max value of the Tree O(losgN + K)
    def kthlargest(self, K):
        if K < 0:
            print('There are not enough elements in the Tree')
            return None
        elif self.NodeCnt//2+1 < K:
            return self.kthsmallest(self.NodeCnt+1-K)
        else:
            stack = []
            node = self.head
            while(stack or node):
                if node:
                    stack.append(node)
                    node = node.rightChild
                else:
                    node = stack.pop()
                    if K == 1:
                        return node.val
                    else:
                        K -= 1
                    node = node.leftChild

    # It returns the min value of the Tree O(logN + K)
    def getMinVal(self, node=-1):
        if node == -1:
            if self.head == None:
                print('No elements in the Tree')
                return float('inf')
            else:
                node = self.head
        if node.leftChild:
            return self.getMinVal(node.leftChild)
        else:
            return node.val

    # It returns the max value of the Tree O(logN)
    def getMaxVal(self, node=-1):
        if node == -1:
            if self.head == None:
                print('No elements in the Tree')
                return float('-inf')
            else:
                node = self.head
        if node.rightChild:
            return self.getMaxVal(node.rightChild)
        else:
            return node.val

    # It returns the number of elements in the Tree O(1)
    def getSize(self):
        return self.NodeCnt
    
    # It returns the height of the Tree O(1)
    def getHeightTree(self):
        if self.head == None:
            return 0
        return self.head.height

    # It returns a list in pre Order of the Tree O(N)
    def preOrder(self, node=-1):
        if node == -1:
            node = self.head
        if node:
            return [node.val] + self.preOrder(node.leftChild) + self.preOrder(node.rightChild)
        else:
            return []

    # It returns a list in Order of the Tree O(N)
    def inOrder(self, node=-1):
        if node == -1:
            node = self.head
        if node:
            return self.inOrder(node.leftChild) + [node.val] + self.inOrder(node.rightChild)
        else:
            return []

    # It returns a list in post Order of the Tree O(N)
    def postOrder(self, node=-1):
        if node == -1:
            node = self.head
        if node:
            return self.postOrder(node.leftChild) + self.postOrder(node.rightChild) + [node.val]
        else:
            return []

    # It updates the place of each node and get the list of nodes in Order O(N)
    def getListInOrder(self, node=-1):
        if node == -1:
            self.count = 0
            node = self.head
            self.listInOrder = []
        if node:
            self.getListInOrder(node.leftChild)
            self.listInOrder.append(node.val)
            node.place = self.count
            self.count += 1
            self.getListInOrder(node.rightChild)

    # It updates the lists of the size of each value of nodes O(N)
    def lenNodes(self):
        self.sizes = []
        self.sumsizes = []
        for x in self.listInOrder:
            self.sizes.append(len(str(x)))
        past = 1
        for x in self.sizes:
            self.sumsizes.append(past)
            past += x
        self.sumsizes.append(past)

    # It returns the full draw of the tree in 2dimensions O(N)
    def __str__(self):
        self.getListInOrder()
        self.lenNodes()
        if self.head == None:
            return 'No elements in the Tree'

        outstr = '\n'
        queue = [self.head]
        while queue:
            aux = []
            past, nextpast = 0, 0
            line, nextline = '', ''
            for q in queue:
                if q.leftChild and q.rightChild:
                    aux.append(q.leftChild)
                    aux.append(q.rightChild)
                    # Print of the _ and the values of the nodes
                    line += ' '*(self.sumsizes[q.leftChild.place+1]-past) + '_'*(self.sumsizes[q.place]-self.sumsizes[q.leftChild.place+1]) + str(q.val) + '_'*(self.sumsizes[q.rightChild.place]-self.sumsizes[q.place+1])
                    past = self.sumsizes[q.rightChild.place]
                    # Print of the arms of the Tree
                    nextline += ' '*(self.sumsizes[q.leftChild.place+1]-nextpast-1) + '/' + ' '*(self.sumsizes[q.rightChild.place]-self.sumsizes[q.leftChild.place+1]) + '\\' + ' '*(self.sizes[q.rightChild.place]-1)
                    nextpast = self.sumsizes[q.rightChild.place+1]
                elif q.leftChild:
                    aux.append(q.leftChild)
                    # Print of the _ and the values of the nodes
                    line += ' '*(self.sumsizes[q.leftChild.place+1]-past) + '_'*(self.sumsizes[q.place]-self.sumsizes[q.leftChild.place+1]) + str(q.val)
                    past = self.sumsizes[q.place+1]
                    # Print of the arms of the Tree
                    nextline += ' '*(self.sumsizes[q.leftChild.place+1]-nextpast-1) + '/'
                    nextpast = self.sumsizes[q.leftChild.place+1]
                elif q.rightChild:
                    aux.append(q.rightChild)
                    # Print of the _ and the values of the nodes
                    line += ' '*(self.sumsizes[q.place]-past)+str(q.val)+'_'*(self.sumsizes[q.rightChild.place]-self.sumsizes[q.place+1])
                    past = self.sumsizes[q.rightChild.place]
                    # Print of the arms of the Tree
                    nextline += ' '*(self.sumsizes[q.rightChild.place]-nextpast) + '\\' + ' '*(self.sizes[q.rightChild.place]-1)
                    nextpast = self.sumsizes[q.rightChild.place+1]
                else:
                    line += ' '*(self.sumsizes[q.place]-past)+str(q.val)
                    past = self.sumsizes[q.place+1]
            # Add the lines to the output string
            outstr += line + '\n' + nextline + '\n'
            queue = aux
        return outstr[:-1]

# It returns the head of the Tree that was build with the plane Tree "s"
def getTree(s):
    if type(s) == str:
        if ',' in s:
            key = ','
            s.replace(' ','')
        else:
            key = ' ' 
        aux = s.split(key)
        key = 'null' if 'null' in aux else ('None' if 'None' in aux else '-1')
        mylist = [None if x == key else int(x) for x in aux]
    elif type(s) == list and 0 < len(s) and type(s[0]) == int:
        mylist = s if None in s else [None if x == -1 else int(x) for x in s]
    else:
        print('Wrong format for the input')
        return None
    # Stars building the tree
    head = TreeNode(mylist[0])
    queue = [head]
    i = 1
    while queue:
        aux = []
        for q in queue:
            if mylist[i] != None:
                q.leftChild = TreeNode(mylist[i])
                aux.append(q.leftChild)
            i += 1
            if mylist[i] != None:
                q.rightChild = TreeNode(mylist[i])
                aux.append(q.rightChild)
            i += 1
        queue = aux
    return head

# It returns the full draw of the tree in 2dimensions O(N)
def getStr(head):
    if head == None:
        return 'No elements in the Tree'
    # Gets the in-order list of the values and its place
    listInOrder, stack = [], []
    node = head
    count = 0
    while(stack or node):
        if node:
            stack.append(node)
            node = node.leftChild
        else:
            node = stack.pop()
            listInOrder.append(node.val)
            node.place = count
            count += 1
            node = node.rightChild
    # Gets the sizes of each node
    sizes, sumsizes = [], []
    for x in listInOrder:
        sizes.append(len(str(x)))
    past = 1
    for x in sizes:
        sumsizes.append(past)
        past += x
    sumsizes.append(past)
    # Builds the output string
    outstr = '\n'
    queue = [head]
    while queue:
        aux = []
        past, nextpast = 0, 0
        line, nextline = '', ''
        for q in queue:
            if q.leftChild and q.rightChild:
                aux.append(q.leftChild)
                aux.append(q.rightChild)
                # Print of the _ and the values of the nodes
                line += ' '*(sumsizes[q.leftChild.place+1]-past) + '_'*(sumsizes[q.place]-sumsizes[q.leftChild.place+1]) + str(q.val) + '_'*(sumsizes[q.rightChild.place]-sumsizes[q.place+1])
                past = sumsizes[q.rightChild.place]
                # Print of the arms of the Tree
                nextline += ' '*(sumsizes[q.leftChild.place+1]-nextpast-1) + '/' + ' '*(sumsizes[q.rightChild.place]-sumsizes[q.leftChild.place+1]) + '\\' + ' '*(sizes[q.rightChild.place]-1)
                nextpast = sumsizes[q.rightChild.place+1]
            elif q.leftChild:
                aux.append(q.leftChild)
                # Print of the _ and the values of the nodes
                line += ' '*(sumsizes[q.leftChild.place+1]-past) + '_'*(sumsizes[q.place]-sumsizes[q.leftChild.place+1]) + str(q.val)
                past = sumsizes[q.place+1]
                # Print of the arms of the Tree
                nextline += ' '*(sumsizes[q.leftChild.place+1]-nextpast-1) + '/'
                nextpast = sumsizes[q.leftChild.place+1]
            elif q.rightChild:
                aux.append(q.rightChild)
                # Print of the _ and the values of the nodes
                line += ' '*(sumsizes[q.place]-past)+str(q.val)+'_'*(sumsizes[q.rightChild.place]-sumsizes[q.place+1])
                past = sumsizes[q.rightChild.place]
                # Print of the arms of the Tree
                nextline += ' '*(sumsizes[q.rightChild.place]-nextpast) + '\\' + ' '*(sizes[q.rightChild.place]-1)
                nextpast = sumsizes[q.rightChild.place+1]
            else:
                line += ' '*(sumsizes[q.place]-past)+str(q.val)
                past = sumsizes[q.place+1]
        # Add the lines to the output string
        outstr += line + '\n' + nextline + '\n'
        queue = aux
    return outstr[:-1]

# it Returns the Tree in its plane form
def getList(Node):
    treeList = []
    stack = [Node]
    while stack:
        q = stack.pop()
        if q:
            treeList.append(q.val)
            stack.append(q.rightChild)
            stack.append(q.leftChild)
        else:
            treeList.append(None)
    return treeList
root = sbbst()
nums = [128, 131, 4, 134, 135, 10, 1, 3, 140, 14, 142, 145, 146, 147, 149] # random numbers
for num in nums:
    root.insert(num)
root.insert(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
# searching the values
valueToSearch = TreeNode(7)
print(root.search(valueToSearch, 7))
valueToSearch = TreeNode(14)
print(root.search(valueToSearch, 14))
print(root)
root.delete(14)
print(root)
# python ./Binary_Tree.py - to run this program