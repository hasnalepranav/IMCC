
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List (Append)
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # 2. Traverse and print nodes
    def display(self):
        temp = self.head

        if temp is None:
            print("Linked List is empty")
            return

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 3. Insert node at a specific position
    # Positions start from 1
    def insert(self, data, position):
        new_node = Node(data)

        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        count = 1

        while temp is not None and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 4. Delete alternate nodes
    # Keep 1st, delete 2nd, keep 3rd, delete 4th...
    def delete_alternate(self):
        temp = self.head

        while temp is not None and temp.next is not None:
            temp.next = temp.next.next
            temp = temp.next


# Main program
ll = LinkedList()

# Create linked list
n = int(input("Enter number of nodes: "))

for i in range(n):
    value = int(input("Enter node value: "))
    ll.append(value)

print("\nOriginal Linked List:")
ll.display()

# Insert a node
value = int(input("\nEnter value to insert: "))
position = int(input("Enter position: "))
ll.insert(value, position)

print("After insertion:")
ll.display()

# Delete alternate nodes
ll.delete_alternate()

print("After deleting alternate nodes:")
ll.display()
