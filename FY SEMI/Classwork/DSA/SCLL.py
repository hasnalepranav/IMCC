class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def insert(self, new_node, pos):
        if pos == 1:   #inserting at first position
            temp = self.head
            while(temp.next != self.head):   #find last node
                temp = temp.next
            new_node.next = self.head
            self.head = new_node
            temp.next = self.head
        else:    #inserting at any other position
            p = 1
            temp = self.head
            while(p != pos - 1):
                temp = temp.next
                p += 1
            new_node.next = temp.next
            temp.next = new_node

           
        

    

    

    def  print(self):
        print()
        print("List element : ")
        temp = self.head
        while(True):
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break


list1 = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
list1.append(n1)
list1.append(n2)
list1.append(n3)
list1.append(Node(40))
list1.print()
list1.insert(Node(5), 1)
list1.print()