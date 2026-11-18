def enqueue(queue):
    element = int(input("Enter element to insert: "))
    queue.append(element)
    print(element, "inserted into queue")


def dequeue(queue):
    if len(queue) == 0:
        print("Queue is empty! Cannot dequeue.")
    else:
        element = queue.pop(0)
        print("Deleted element:", element)


def display(queue):
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("\nQueue elements:")
        print("FRONT →", end=" ")

        for element in queue:
            print(element, end=" → ")

        print("REAR")


def reverse_queue(queue):
    if len(queue) == 0:
        print("Queue is empty")
        return queue

    stack = []

    while len(queue) > 0:
        stack.append(queue.pop(0))

    while len(stack) > 0:
        queue.append(stack.pop())

    print("Queue reversed successfully.")

    return queue


def merge_queues(queue1, queue2):
    merged_queue = queue1 + queue2

    print("Merged Queue:", merged_queue)

    return merged_queue


def check_identical(queue1, queue2):
    if queue1 == queue2:
        print("Both queues are identical.")
    else:
        print("Both queues are not identical.")


def main():

    queue1 = []
    queue2 = []

    while True:

        print("\nLINEAR QUEUE OPERATIONS")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Reverse Queue using Stack")
        print("5. Merge Two Queues")
        print("6. Check if Two Queues are Identical")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            q = int(input("Enter queue number (1 or 2): "))

            if q == 1:
                enqueue(queue1)
            elif q == 2:
                enqueue(queue2)
            else:
                print("Invalid queue number")

        elif choice == 2:

            q = int(input("Enter queue number (1 or 2): "))

            if q == 1:
                dequeue(queue1)
            elif q == 2:
                dequeue(queue2)
            else:
                print("Invalid queue number")

        elif choice == 3:

            print("\nQueue 1:")
            display(queue1)

            print("\nQueue 2:")
            display(queue2)

        elif choice == 4:

            q = int(input("Enter queue number (1 or 2): "))

            if q == 1:
                queue1 = reverse_queue(queue1)
            elif q == 2:
                queue2 = reverse_queue(queue2)
            else:
                print("Invalid queue number")

        elif choice == 5:

            queue1 = merge_queues(queue1, queue2)
            queue2 = []

            print("Queue 1 now contains the merged elements.")
            print("Queue 2 is now empty.")

        elif choice == 6:

            check_identical(queue1, queue2)

        elif choice == 7:

            print("Exiting Queue Program...")
            break

        else:
            print("Invalid choice! Try again.")


main()