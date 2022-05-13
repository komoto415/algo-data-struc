"""
insert
delete
search

insert(10)
      10

insert(4)
      10
   4

insert(15)
      10
   4    15

insert(5)
      10
   4    15
     5

insert(9)
      10
    4   15
     5
      9

insert(5)
      10
    4   15
     5
      9
     5

insert(3)

      10
    4   15
     5
      9
     5
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        str = f"{self.key}\n"
        if self.left:
            str += f"{self.left.key}   "
        else:
            str += "   "
        if self.right:
            str += f"{self.right.key}   "
        else:
            str += "   "
        return str

class BinarySearchTree:
    def __init__(self):
        self.size = 0
        self.root = None

    def insert(self, ele):
        if self.size == 0:
            self.root = ele
            self.size += 1
            return

        current_node = None
        search_node = self.root
        while search_node is not None:
            current_node = search_node
            if ele.key < search_node.key:
                search_node = search_node.left
            else:
                search_node = search_node.right
        ele.parent = current_node
        if ele.key < current_node.key:
            current_node.left = ele
        else:
            current_node.right = ele
        self.size += 1

    def delete(self, key):
        ...

    def contains(self, key):
        if self.root is None:
            return False
        if key == self.root.key:
            return True

        search_node = self.root
        while search_node is not None:
            print(search_node)
            if search_node.key == key:
                return True
            if key < search_node.key:
                search_node = search_node.left
            else:
                search_node = search_node.right
        return False

    def min(self):
        if self.root is None:
            return None

        search_node = self.root
        while search_node.left is not None:
            search_node = search_node.left
        return search_node

    def max(self):
        if self.root is None:
            return None

        search_node = self.root
        while search_node.right is not None:
            search_node = search_node.right
        return search_node

    def show(self):
        self.__go(self.root)

    def __go(self, node):
        if self.root is None:
            print("Empty")
            return
        print(node.key)
        if node.left is None and node.right is None:
            return
        if node.left:
            self.__go(node.left)
        if node.right:
            self.__go(node.right)

def main():
    bst = BinarySearchTree()
    # bst.show()
    print(bst.max())
    bst.insert(Node(10))
    # bst.show()
    bst.insert(Node(4))
    # bst.show()
    bst.insert(Node(15))
    # bst.show()
    bst.insert(Node(5))
    # bst.show()
    bst.insert(Node(9))
    # bst.show()
    bst.insert(Node(5))
    # bst.show()
    bst.insert(Node(3))
    # bst.show()
    bst.insert((Node(20)))
    print(bst.max().key)

    # print(bst.contains(9))

if __name__ == "__main__":
    main()
