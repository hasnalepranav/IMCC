
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        temp = self.head

        if temp:
            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp
        else:
            self.head = new_node

    def print(self):
        temp = self.head
        print("List elements:", end=" ")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


list1 = LinkedList()
list1.append(Node(12))
list1.append(Node(52))
list1.append(Node(102))
list1.append(Node(56))

list1.print()
