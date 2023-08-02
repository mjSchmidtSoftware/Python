"""
Jordan Jones jbjones
Michael James Schmidt mjschmid
CMPS101
hw6
5-20-16

implement Binary Search Tree BSTree
RBTree for extra credit

"""
#import heapq as hq
#NUMBER 1
#/////////////////////////////////////////////////////////////////////////////////////////////////////////
class Node:
    # Node constructor
    #key represents a word, value represents the frequency of word
    #all keys will be distinct
    def __init__(self, key, value, parent=None, left=None, right=None):
        self.key = key  # key
        self.value = value  # data
        self.parent = parent  # parent node
        self.left = left  # left child
        self.right = right  # right child
#////END_CLASS_NODE/////////////////////////////////////////////////////////////////////////////////////////////////////
#///CLASS_BSTREE////////////////////////////////////////////////////////////////////////////////////////////////////////
class BSTree:
    def __init__(self):                             # BSTree constructor
        self.root = None                            # there is no root when the tree is created

#////INSERT()///////////////////////////////////////
    def insert(self, key, value):                   # insert function
        if self.root == None:                       # if there is no root
            self.root = Node(key, value)            # make the newNode the root
            return                                  # all done get out of insert
      
        current_node = self.root                    # set the current node to the root
        while True:                                 # While loop
            #if key is already in tree
            #increment value and don't insert            
            if key == current_node.key:
                current_node.value = current_node.value + 1
                return
            #otherwise insert
            elif key < current_node.key:              # if true go left
                if current_node.left:               # if there is a node to go to then go there
                    current_node = current_node.left
                else:                               # else you reached the end of the line
                    current_node.left = Node(key, value, current_node) # put the new node on the current_nodes left child
                    return                          # all done get out of insert
            elif key > current_node.key:                                   #else go right
                if current_node.right:              # if there is a node to go to then go there
                    current_node = current_node.right
                else:                               #else you reached the end of the line
                    current_node.right = Node(key, value, current_node) # put the new node on the current_nodes right child
                    return                          # all done get out of insert
#////END_INSERT()///////////////////////////////////
#////IN_ORDER_TRAVERSAL/////////////////////////////
    def inOrderTraversal(self):                     #in order traversal done without recursion
        #f = open ("Lo_Trav.txt", 'w')
        
        if self.root == None:
            print('nothing in the tree!')
        else:
            stack = []                                  # stack to hold the keys
            current_node = self.root                    #start at the tree root
            solution = []                               # hold list of the keys that are in Order from least to greatest
            while current_node != None or len(stack) > 0:
                if current_node != None:
                    stack.append(current_node)
                    current_node = current_node.left    # keep going left until their is no node
                else:
                    current_node = stack.pop()          #node is now the last item to be pushed onto the stack
                    solution.append(current_node)   #found lowest key that was not been pushed onto the stack
                    current_node = current_node.right   # now go right
                
                #print(solution)
            #return solution
            for i in range(0, len(solution)):
                #f.write(str(solution[i].key)+", "+str(solution[i].value)+" \n")
                print("KEY: ",str(solution[i].key),", VAL: " ,str(solution[i].value))
            #f.close()
# ////END_IN_ORDER_TRAVERSAL///////////////////////
#/////FIND///////////////////////////////////////////
    #finds a node with key and returns it
    def find(self, key):                        # the find is very similar to the traversal function
        current = self.root
        while current.key != key:
            if key < current.key:               # go left
                current = current.left
            else:                               # else you have to go right
                current = current.right
            if current == None:
                return None                     # did not find
        #print(current.value)
        return current
#////END_FIND/////////////////////////////////////////
#////SUCCESSOR////////////////////////////////////////
    #returns successor of node with key    
    #if node doesn't exist, returns its parent's successor
    def successor(self, key):
        node = self.find(key)
        parent = node.parent
        if node.right != None:
            x = node.right
            while x.left != None: #find min of Tree
                x = x.left
            return x
        current = parent
        while current != None and node == current.right:
            node = current
            current = current.parent
        return current

#////END_SUCCESSOR////////////////////////////////////
#////DELETE///////////////////////////////////////////
    def transplant(self,u,v):             # transplant moves sub trees around
        if u.parent == None:              #replaces one subtree as a child of the parent
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent

    def minimum(self,node):             #find min of tree
        while node.left != None:
            node = node.left
        return node


    def delete(self,key):              #delete function takes in the key of the node that is being deleted
        delNode = self.find(key)
        #delParent = delNode.parent
        if delNode == None:             # if there is nothing in the tree just return
            print ("There are nodes in this tree to delete")
            return
        if delNode.left == None:
            self.transplant(delNode, delNode.right) #transplant right
        elif delNode.right == None:
            self.transplant(delNode, delNode.left)  #transplant left
        else:
            minimum = self.minimum(delNode.right)
            if minimum.parent != delNode:
                self.transplant(minimum,minimum.right)
                minimum.right = delNode.right
                minimum.right.parent = minimum
            self.transplant(delNode,minimum)
            minimum.left = delNode.left
            minimum.left.parent = minimum
#////END_DELETE///////////////////////////////////////

"""

#build 2 binary search trees, 
#one for low ratings (1-3) and the other for high ratings (4-5).  
#Each tree stores all words that occurring in reviews of those ratings.  Each tree
#stores a single node for each distinct word, and maintains the frequency as the value.  
#So, (say) tree 1 will have a node with key \dog", 
#whose value stores the nuber of times that "dog" appears in1-3 stars ratings.

Low_T = BSTree() # 1-3 star ratings
High_T = BSTree() #4-5  star ratings

# NUMBER 2 -----------------------------------------------------------
print("start execution")
#process stopwords.txt, 
#store words in a standard set object
stopWords = set()
with open('stopwords.txt','r') as f:
    for line in f:
        for word in line.split():
            #print(word)
            stopWords.add(word)
    f.close()

#process finefoods_cleaned.txt and put into proper BSTrees
with open('finefoods_cleaned.txt','r') as g:
    # initialize ratings as false
    for line in g:
        high_rate = False
        low_rate = False
        for word in line.split():
            # determine rating
            if word == "4:" or word == "5:":  # 4-5 star review 
                high_rate = True
                low_rate = False
            elif word == "1:" or word == "2:" or word == "3:":  # 1-3 star review
                low_rate = True
                high_rate = False
            #insert if not in stopWords    
            elif word not in stopWords: #and word != "1:" and word != "2:" and word != "3:" and word != "4:" and word != "4:" and word != "5:":
                #if high rated review                    
                if high_rate == True:
                    High_T.insert(word, 1)
                    #if High_T.root == None:     #unnneccesary this check is in insert
                        #High_T.insert(word, 1)
                    #elif High_T.find(word) != 0:  # if true then the update frequency
                        #print()
                        # NOT DONE update the frequency in insert
                    #else:
                    #    High_T.insert(word, 1)  # else it not in the tree so insert it
                #insert low rated review
                elif low_rate == True:
                    Low_T.insert(word, 1)
                        #if Low_T.root == None:  # nothing in the tree so Insert
                        #    Low_T.insert(word, 1)
                        #elif Low_T.find(word) != 0:  # if true then the update frequency
                        #    print()
                            # NOT DONE update the frequency in insert
                        #else:
                        #    Low_T.insert(word, 1)  # else it not in the tree so insert it
    g.close()

#print("High_T---------------------------------")
#High_T.inOrderTraversal()
#print("Low_T----------------------------------")
#Low_T.inOrderTraversal()

#NUMBER 3 --------------------------------------------
#determine if in tree and its frequency,
#if not, find its successor and its freq
#asymptotic
#binary
#complexity
#depth
#mergesort
#quicksort
#structure
#theta
#put info in finds.txt

#find the word's parent's successor and its frequency
#does number 3
def num3(key):
    print("-------------",key,"------------")
    H = High_T.find(key)
    L = Low_T.find(key)
    
    if H == None:
        High_T.insert(key,0)
        H = High_T.successor(key)
        High_T.delete(key)
    if L == None:
        Low_T.insert(key,0)
        L = Low_T.successor(key)
        Low_T.delete(key)
    if H != None:
        print("HIGH_T")
        print(H.key, H.value)
    if L != None:
        print("LOW_T")
        print(L.key, L.value)
        
        
#num3("asymptotic")
#num3("binary")
#num3("complexity")
#num3("depth")
#num3("mergesort")
#num3("quicksort")
#num3("structure")
#num3("theta")
#tree = BSTree()
#tree.insert(10,1)
#tree.insert(5,1)
#tree.insert(6,1)
#tree.insert(1,1)
#tree.insert(12,1)
#tree.insert(11,1)

#High_T.inOrderTraversal()
#Low_T.inOrderTraversal()
print("done with tree insertions")

#NUMBER 4
#Perform a traversal of each tree, and determine the top 20 most
#frequent words (for low rating and high rating).  Then, take all the words
#in the low rating tree,  and delete them from the high rating tree.  How
#many distinct words are left?  What is new top 20 most frequent words?
#Submit a  file frequent.txt with all this information.
#use heapq object 

#heap for low rating
LR_hp = []
#heap for high rating
HR_hp = []
solH = High_T.inOrderTraversal()
#solL = Low_T.inOrderTraversal()

#f = open("inOrder_HI.txt", "w")
#High_T.inOrderTraversal()
#f.write()

for i in range(len(solH)):
    #turn nodes into tuples of key and value
    tupH = (solH[i].value, solH[i].key)
    hq.heappush(HR_hp, tupH)
    hq.heapify(HR_hp)
#for j in range(len(solL)):
#    tupL = (solL[j].value, solL[j].key)
#    hq.heappush(LR_hp, tupL)
#    hq.heapify(LR_hp)
    
#for k in range(len(HR_hp)):
#    print(str(HR_hp[k]))
    
#print 20 largest from high rate tree
print("20 LARGESTTTTT High")
print(hq.nlargest(20,HR_hp))
#print 20 largest from low rate tree   
#print("20 LARGESTTTTT Low")
#print(hq.nlargest(20,LR_hp))

print("DONE")

"""