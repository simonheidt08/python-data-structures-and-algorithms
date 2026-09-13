import random
class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.count = 1
        self.priority = random.random()


def rotate_left(t):
    x = t.right
    t.right = t.right.left
    x.left = t
    return x

def rotate_right(t):
    x = t.left
    t.left = t.left.right
    x.right = t
    return x

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
            if node.priority < node.left.priority:
                node = rotate_right(node)
        elif key > node.key:
            node.right = self._insert(node.right, key)
            if node.priority < node.right.priority:
                node = rotate_left(node)
        else:
            node.count += 1
        return node
    
    def delete(self, key):
        self.root = self._delete(self.root, key)
    
    def _delete(self, node, key):
        if not node:
            return None
        elif key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.count > 1: node.count -= 1
            else:
                if not node.left: return node.right
                elif not node.right: return node.left
                else:
                    if node.right.priority > node.left.priority:
                        node = rotate_left(node)
                        node.left = self._delete(node.left, key)
                    else:
                        node = rotate_right(node)
                        node.right = self._delete(node.right, key)
        return node
    
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node or key == node.key:
            return node
        elif key < node.key:
            return self._search(node.left, key)
        elif key > node.key:
            return self._search(node.right, key)
        
    def order(self):
        result = []
        self._order(self.root, result)
        return result
    
    def _order(self, node, result):
        if node:
            self._order(node.left, result)
            result.extend([node.key]*node.count)
            self._order(node.right, result)

    def tree_order(self):
        printing = str(self.root.key)
        l1 = [self.root]
        l2 = []
        while any(x for x in l1):
            printing += "\n"
            for i in l1:
                if i:
                    if i.left:
                        printing += f"{i.left.key} "
                    else:
                        printing += "* "
                    if i.right:
                        printing += f"{i.right.key} "
                    else:
                        printing += "* "
                    l2.extend([i.left, i.right])
                else:
                    printing += "* * "
                    l2.extend([None, None])
            l1 = l2
            l2 = []
        return printing

def tree_formatter(tree):

    def letter_split(line, n):
            letters = line.split(" ")
            for j in range(1,len(letters)):
                letters[j] = " "*(2**(len(lines)-n)-len(letters[j])) + letters[j]
            line = "".join(letters)
            return line
    
    lines = tree.split("\n")
    del lines[-1]
    for i in range(len(lines)):
        lines[i] = letter_split(lines[i], i)
        lines[i] = " "*(2**(len(lines)-i-1)-1) + lines[i]

    formatted_tree = "\n".join(lines)
    return formatted_tree

my_bst = BST()
test_list = [8,4,12,2,6,10,14]
for i in test_list:
    my_bst.insert(i)
    print(tree_formatter(my_bst.tree_order()))
for i in test_list:
    print(tree_formatter(my_bst.tree_order()))
    my_bst.delete(i)