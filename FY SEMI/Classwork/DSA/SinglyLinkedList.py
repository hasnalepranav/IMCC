class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def delfirst_last(self):
        temp=None
    def delete_alternate(self):
        prev=self.head
        temp=self.head.next
        while prev and temp:
            prev.next=temp.next
            temp=None
            prev=prev.next
            if prev:
                temp=prev.next
    def print(self):
        print()
        print("List elements")

        
