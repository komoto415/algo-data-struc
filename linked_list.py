'''
size
insert
delete
get
contains
'''

from operator import truediv


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        str = f"({self.data} -> "
        if self.next is not None:
            str += f"{self.next.data})"
        else:
            str+= "None)"
        return str

class LinkedList:
    def __init__(self):
        self.__num_elements = 0
        self.__head = None

    def size(self):
        return self.__num_elements
    
    def insert(self, ele):
        if self.__num_elements == 0:
            self.__head = Node(ele)
            self.__num_elements += 1
            return
        current_node = self.__head

        # while True:
        #     if current_node.next is None:
        #         current_node.next = Node(ele)
        #         self.__num_elements += 1
        #         break
        #     else:
        #         current_node = current_node.next

    def delete(self, ele):
        assert self.__num_elements > 0

        current_node = self.__head

        while True:
            ...

    def deep_str(self):
        current_node = self.__head
        for i in range(self.__num_elements):
            print(current_node)
            current_node = current_node.next

    def __str__(self):
        str = "["
        current_node = self.__head
        for i in range(self.__num_elements):
            str += f"{current_node.data}{', ' if i < self.__num_elements-1 else ''}"
            current_node = current_node.next
        str += "]"
        return str

def main():
    ll = LinkedList()
    ll.insert("1")
    ll.insert("2")
    ll.insert("3")
    ll.insert("4")
    ll.insert("5")
    ll.insert("6")
    ll.insert("7")
    print(ll.size())
    print(ll)
    ll.deep_str()

if __name__ == "__main__":
    main()
            


