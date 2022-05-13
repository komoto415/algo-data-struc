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

class BinarySearchTree:
    def __init__(self):
        self.size = 0
        self.root = None

    def insert(self, data):
        if self.size == 0:
            self.root = data
            return

        current_node = None
        search_node = self.root
        while search_node is not None:
            current_node = search_node
            if data.key < search_node.key:
                search_node = search_node.left
            else:
                search_node = search_node.right
        data.parent = current_node
        if data.key < current_node.key:
            current_node.left = data
        else:
            current_node.right = data
        self.size += 1

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
    bst.show()


if __name__ == "__main__":
    main()