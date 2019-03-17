# bintree.py
# Raunak Anand
# This program creates a binary tree using words in a .txt file 

class Node: # creating class Node 

    def __init__(self, data, count = 1):

        self.left = None
        self.right = None
        self.data = data
        self.count = count

    def __str__(self): # how each word should be printed
        return str(self.data)+"("+str(self.count)+")" 
  
def node_creation(root, data):
# Comparing the new value with the parent node to create tree

    if root.data < data:
        if root.right is None:
            root.right = Node(data)  # if nothing is there
                                     # new node is created
        else:
            node_creation(root.right, data) # recursion
    elif root.data > data:
        if root.left is None:
            root.left = Node(data)  # if nothing is there
                                    # new node is created
        else:
            node_creation(root.left, data) # recursion
    else:
        root.count += 1 # if word exists
                        #then word count of the same increases 

def BinTree(node, level): # print only if there is no node
    if node is not None:
        BinTree(node.left, level+1)
        print("  "*level + str(node))
        BinTree(node.right, level+1)

def lst(s, sep): # function to split function
    stack = [s]
    for char in sep:
        pieces = []
        for substr in stack:
            pieces.extend(substr.split(char))
        stack = pieces
    return stack

def main():
    # checking to see if the file exists or not
    try:
        filename = input("What .txt file would you like to make a binary tree of?: ")
        infile = open(filename, "r")

    except:
        print("File doesn't exist sorry!")
        exit()

    x = infile.read()
    # splitting using special characters
    from string import punctuation
    character = list(punctuation)
    character.remove("_")
    character.append(" ")
    character.append("\n")

    words = lst(x,character)
    while "" in words:
        words.remove("")
                

    rootnode = Node(words[0])
    for i in range(1,len(words)): 
        node_creation(rootnode, words[i]) # for all words in the list created 
        
    BinTree(rootnode, 0)

main()

