import random
class TreeNode():
    # It instantiates the class
    def __init__ (self, data):
        self.data = data
        self.place = 0
        self.height = 1
        self.leftChild = None
        self.rightChild = None

# Self Balancing Binary Search Tree based on the type of AVL Trees
class TreeClass():
    # It instantiates the class O(1)
    def __init__(self, dataslist = None):
        self.root = None
        self.NodeCnt = 0
        self.count = 0
        self.sizes = []
        self.allnodes = []
        self.listnode = []
        if type(dataslist) == list:
            for data in dataslist:
                self.root = self.insertNode(self.root, data)

    # It return True if the data is found, False otherwhise O(logN)
    def search(self, node, data):
        if not node:
            return False
        else:
            if node.data < data:
                return self.search(node.rightChild, data)
            elif data < node.data:
                return self.search(node.leftChild, data)
            else:
                return True

    # It inserts a node and updates the root node O(logN)
    def insert(self, data):
        self.root = self.insertNode(self.root, data)
    
    # It inserts a node with a dataue and returns the node of the modified subtree O(logN)
    def insertNode(self, node, data):
        # Step 1 - Perform normal BST
        if not node:
            self.NodeCnt += 1
            return TreeNode(data)
        
        elif data < node.data:
            node.leftChild = self.insertNode(node.leftChild, data)
        else:
            node.rightChild = self.insertNode(node.rightChild, data)
        
        # 2: Update the height of the node
        node.height = 1 + max(self.getHeight(node.leftChild), self.getHeight(node.rightChild))
        # 3: Get the balance factor
        balance = self.getBalance(node)
        # 4: If the node is unbalanced, try out the 2 cases
        if balance > 1: # Case 1: leftChild (leftChild/rightChild)
            if data > node.leftChild.data:
                node.leftChild = self.leftChildRotate(node.leftChild)
            return self.rightChildRotate(node)
        if balance < -1: # Case 2: rightChild (leftChild/rightChild)
            if data < node.rightChild.data:
                node.rightChild = self.rightChildRotate(node.rightChild)
            return self.leftChildRotate(node)
        # Return the result node
        return node

    # It deletes a node with a certain dataue and updates the root node O(logN)
    def delete(self, data):
        self.root = self.deleteNode(self.root, data)

    # It deletes a node with a certain dataue and returns the node of the modified subtree O(logN)
    def deleteNode(self, node, data):
        # 1: Standard BST delete
        if not node:
            return node

        elif data < node.data:
            node.leftChild = self.deleteNode(node.leftChild, data)
        elif data > node.data:
            node.rightChild = self.deleteNode(node.rightChild, data)

        else: # data == node.data            
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
                temp = self.getMindataueNode(node.rightChild)
                node.data = temp.data
                node.rightChild = self.deleteNode(node.rightChild, temp.data)

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
    def getMindataueNode(self, node):
        if node is None or node.leftChild is None:
            return node
        return self.getMindataueNode(node.leftChild)

    # It returns the min dataue of the Tree O(logN + K)
    def kthsmallest(self, K):
        if K < 0:
            print('There are not enough elements in the Tree')
            return None
        elif self.NodeCnt//2+1 < K:
            return self.kthlargest(self.NodeCnt+1-K)
        else:
            stack = []
            node = self.root
            while(stack or node):
                if node:
                    stack.append(node)
                    node = node.leftChild
                else:
                    node = stack.pop()
                    if K == 1:
                        return node.data
                    else:
                        K -= 1
                    node = node.rightChild
    
    # It returns the max dataue of the Tree O(losgN + K)
    def kthlargest(self, K):
        if K < 0:
            print('There are not enough elements in the Tree')
            return None
        elif self.NodeCnt//2+1 < K:
            return self.kthsmallest(self.NodeCnt+1-K)
        else:
            stack = []
            node = self.root
            while(stack or node):
                if node:
                    stack.append(node)
                    node = node.rightChild
                else:
                    node = stack.pop()
                    if K == 1:
                        return node.data
                    else:
                        K -= 1
                    node = node.leftChild

    # It returns the min dataue of the Tree O(logN + K)
    def getMindata(self, node=-1):
        if node == -1:
            if self.root == None:
                print('No elements in the Tree')
                return float('inf')
            else:
                node = self.root
        if node.leftChild:
            return self.getMindata(node.leftChild)
        else:
            return node.data

    # It returns the max dataue of the Tree O(logN)
    def getMaxdata(self, node=-1):
        if node == -1:
            if self.root == None:
                print('No elements in the Tree')
                return float('-inf')
            else:
                node = self.root
        if node.rightChild:
            return self.getMaxdata(node.rightChild)
        else:
            return node.data

    # It returns the number of elements in the Tree O(1)
    def getSize(self):
        return self.NodeCnt
    
    # It returns the height of the Tree O(1)
    def getHeightTree(self):
        if self.root == None:
            return 0
        return self.root.height

    # It returns a list in pre Order of the Tree O(N)
    def preOrder(self, node=-1):
        if node == -1:
            node = self.root
        if node:
            return [node.data] + self.preOrder(node.leftChild) + self.preOrder(node.rightChild)
        else:
            return []

    # It returns a list in Order of the Tree O(N)
    def inOrder(self, node=-1):
        if node == -1:
            node = self.root
        if node:
            return self.inOrder(node.leftChild) + [node.data] + self.inOrder(node.rightChild)
        else:
            return []

    # It returns a list in post Order of the Tree O(N)
    def postOrder(self, node=-1):
        if node == -1:
            node = self.root
        if node:
            return self.postOrder(node.leftChild) + self.postOrder(node.rightChild) + [node.data]
        else:
            return []

    # It updates the place of each node and get the list of nodes in Order O(N)
    def getlistnode(self, node=-1):
        if node == -1:
            self.count = 0
            node = self.root
            self.listnode = []
        if node:
            self.getlistnode(node.leftChild)
            self.listnode.append(node.data)
            node.place = self.count
            self.count += 1
            self.getlistnode(node.rightChild)

    # It updates the lists of the size of each dataue of nodes O(N)
    def lenNodes(self):
        self.sizes = []
        self.allnodes = []
        for x in self.listnode:
            self.sizes.append(len(str(x)))
        past = 1
        for x in self.sizes:
            self.allnodes.append(past)
            past += x
        self.allnodes.append(past)

    # It returns the full draw of the tree in 2dimensions O(N)
    def __str__(self):
        self.getlistnode()
        self.lenNodes()
        if self.root == None:
            return 'No elements in the Tree'

        outstr = '\n'
        queue = [self.root]
        while queue:
            aux = []
            past, nextpast = 0, 0
            line, nextline = '', ''
            for q in queue:
                if q.leftChild and q.rightChild:
                    aux.append(q.leftChild)
                    aux.append(q.rightChild)
                    # Print of the _ and the dataues of the nodes
                    line += ' '*(self.allnodes[q.leftChild.place+1]-past) + '_'*(self.allnodes[q.place]-self.allnodes[q.leftChild.place+1]) + str(q.data) + '_'*(self.allnodes[q.rightChild.place]-self.allnodes[q.place+1])
                    past = self.allnodes[q.rightChild.place]
                    # Print of the arms of the Tree
                    nextline += ' '*(self.allnodes[q.leftChild.place+1]-nextpast-1) + '/' + ' '*(self.allnodes[q.rightChild.place]-self.allnodes[q.leftChild.place+1]) + '\\' + ' '*(self.sizes[q.rightChild.place]-1)
                    nextpast = self.allnodes[q.rightChild.place+1]
                elif q.leftChild:
                    aux.append(q.leftChild)
                    # Print of the _ and the dataues of the nodes
                    line += ' '*(self.allnodes[q.leftChild.place+1]-past) + '_'*(self.allnodes[q.place]-self.allnodes[q.leftChild.place+1]) + str(q.data)
                    past = self.allnodes[q.place+1]
                    # Print of the arms of the Tree
                    nextline += ' '*(self.allnodes[q.leftChild.place+1]-nextpast-1) + '/'
                    nextpast = self.allnodes[q.leftChild.place+1]
                elif q.rightChild:
                    aux.append(q.rightChild)
                    # Print of the _ and the dataues of the nodes
                    line += ' '*(self.allnodes[q.place]-past)+str(q.data)+'_'*(self.allnodes[q.rightChild.place]-self.allnodes[q.place+1])
                    past = self.allnodes[q.rightChild.place]
                    # Print of the arms of the Tree
                    nextline += ' '*(self.allnodes[q.rightChild.place]-nextpast) + '\\' + ' '*(self.sizes[q.rightChild.place]-1)
                    nextpast = self.allnodes[q.rightChild.place+1]
                else:
                    line += ' '*(self.allnodes[q.place]-past)+str(q.data)
                    past = self.allnodes[q.place+1]
            # Add the lines to the output string
            outstr += line + '\n' + nextline + '\n'
            queue = aux
        return outstr[:-1]

# It returns the root of the Tree that was build with the plane Tree "s"
def getTree(s):
    if type(s) == str:
        if ',' in s:
            data = ','
            s.replace(' ','')
        else:
            data = ' ' 
        aux = s.split(data)
        data = 'null' if 'null' in aux else ('None' if 'None' in aux else '-1')
        mylist = [None if x == data else int(x) for x in aux]
    elif type(s) == list and 0 < len(s) and type(s[0]) == int:
        mylist = s if None in s else [None if x == -1 else int(x) for x in s]
    else:
        print('Wrong format for the input')
        return None
    # Stars building the tree
    root = TreeNode(mylist[0])
    queue = [root]
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
    return root

# It returns the full draw of the tree in 2dimensions O(N)
def getStr(root):
    if root == None:
        return 'No elements in the Tree'
    # Gets the in-order list of the dataues and its place
    listnode, stack = [], []
    node = root
    count = 0
    while(stack or node):
        if node:
            stack.append(node)
            node = node.leftChild
        else:
            node = stack.pop()
            listnode.append(node.data)
            node.place = count
            count += 1
            node = node.rightChild
    # Gets the sizes of each node
    sizes, allnodes = [], []
    for x in listnode:
        sizes.append(len(str(x)))
    past = 1
    for x in sizes:
        allnodes.append(past)
        past += x
    allnodes.append(past)
    # Builds the output string
    outstr = '\n'
    queue = [root]
    while queue:
        aux = []
        past, nextpast = 0, 0
        line, nextline = '', ''
        for q in queue:
            if q.leftChild and q.rightChild:
                aux.append(q.leftChild)
                aux.append(q.rightChild)
                # Print of the _ and the dataues of the nodes
                line += ' '*(allnodes[q.leftChild.place+1]-past) + '_'*(allnodes[q.place]-allnodes[q.leftChild.place+1]) + str(q.data) + '_'*(allnodes[q.rightChild.place]-allnodes[q.place+1])
                past = allnodes[q.rightChild.place]
                # Print of the arms of the Tree
                nextline += ' '*(allnodes[q.leftChild.place+1]-nextpast-1) + '/' + ' '*(allnodes[q.rightChild.place]-allnodes[q.leftChild.place+1]) + '\\' + ' '*(sizes[q.rightChild.place]-1)
                nextpast = allnodes[q.rightChild.place+1]
            elif q.leftChild:
                aux.append(q.leftChild)
                # Print of the _ and the dataues of the nodes
                line += ' '*(allnodes[q.leftChild.place+1]-past) + '_'*(allnodes[q.place]-allnodes[q.leftChild.place+1]) + str(q.data)
                past = allnodes[q.place+1]
                # Print of the arms of the Tree
                nextline += ' '*(allnodes[q.leftChild.place+1]-nextpast-1) + '/'
                nextpast = allnodes[q.leftChild.place+1]
            elif q.rightChild:
                aux.append(q.rightChild)
                # Print of the _ and the dataues of the nodes
                line += ' '*(allnodes[q.place]-past)+str(q.data)+'_'*(allnodes[q.rightChild.place]-allnodes[q.place+1])
                past = allnodes[q.rightChild.place]
                # Print of the arms of the Tree
                nextline += ' '*(allnodes[q.rightChild.place]-nextpast) + '\\' + ' '*(sizes[q.rightChild.place]-1)
                nextpast = allnodes[q.rightChild.place+1]
            else:
                line += ' '*(allnodes[q.place]-past)+str(q.data)
                past = allnodes[q.place+1]
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
            treeList.append(q.data)
            stack.append(q.rightChild)
            stack.append(q.leftChild)
        else:
            treeList.append(None)
    return treeList
root = TreeClass()
nums = []
for i in range(0,40):
    element = random.randint(1,300)
    nums.append(element)
for num in nums:
    root.insert(num)
root.insert(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
# searching the dataues
dataueToSearch = TreeNode(7)
print(root.search(dataueToSearch, 7))
dataueToSearch = TreeNode(14)
print(root.search(dataueToSearch, 14))
print(root)
root.delete(14)
print(root)
# python ./Binary_Tree.py - to run this program
# OUTPUT: 
#True
#True
#
#          __________128_________
#         /                      \
#    ____14____               ___140___
#   /          \             /         \
#  _4        __27__        134         145___
# /  \      /      \      /   \       /      \
# 1  10    14      35   131   135   142      147
#  \   \     \    /                         /   \
#  3   10    19  31                       146   149
#
#
#          ________128_________
#         /                    \
#    ____14__               ___140___
#   /        \             /         \
#  _4        27__        134         145___
# /  \      /    \      /   \       /      \
# 1  10    19    35   131   135   142      147
#  \   \        /                         /   \
#  3   10      31                       146   149
#
#True
#True
#
#                        ________________89_________________________________________
#                       /                                                           \
#              ________35______                                _____________________176_________
#             /                \                              /                                 \
#      ______18____          __43____              _________130_________                     ___207_________
#     /            \        /        \            /                     \                   /               \
#  __11__          31      42      __51         109___               ___154___            185            ___267
# /      \        /  \    /  \    /    \       /      \             /         \          /   \          /      \
# 2      14      27  33  35  43  49    80    100      126         148         155      180   190      244      276
#  \    /  \    /                  \        /        /   \       /   \       /   \                   /   \        \
#  10  14  15  19                  50      90      123   128   142   152   154   163               234   256      300
#
#
#                      ________________89_________________________________________
#                     /                                                           \
#            ________35______                                _____________________176_________
#           /                \                              /                                 \
#      ____18____          __43____              _________130_________                     ___207_________
#     /          \        /        \            /                     \                   /               \
#  __11__        31      42      __51         109___               ___154___            185            ___267
# /      \      /  \    /  \    /    \       /      \             /         \          /   \          /      \
# 2      15    27  33  35  43  49    80    100      126         148         155      180   190      244      276
#  \    /     /                  \        /        /   \       /   \       /   \                   /   \        \
#  10  14    19                  50      90      123   128   142   152   154   163               234   256      300
