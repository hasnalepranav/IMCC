
def display(stack):
    if len(stack) == 0:
        print("\nStack is EMPTY")
    else:
        print("\nCurrent Stack:")
        print("TOP")
        for i in range(len(stack) - 1, -1, -1):
            print("|", stack[i], "|")
        print("-----")


def push(stack):
    element = int(input("Enter element to push: "))
    stack.append(element)

    print("\nOperation performed: PUSH")
    print("Inserted element:", element)
    display(stack)


def pop_element(stack):
    if len(stack) == 0:
        print("\nStack is EMPTY. Cannot perform POP.")
    else:
        element = stack.pop()

        print("\nOperation performed: POP")
        print("Removed element:", element)
        display(stack)


def reverse_string():
    string = input("Enter a string: ")
    temp_stack = []

    for char in string:
        temp_stack.append(char)

    reversed_string = ""

    while len(temp_stack) > 0:
        reversed_string += temp_stack.pop()

    print("\nOperation performed: REVERSE STRING")
    print("Original String:", string)
    print("Reversed String:", reversed_string)


def reverse_stack(stack):
    if len(stack) == 0:
        print("\nStack is EMPTY. Cannot reverse.")
        return stack

    another_stack = []

    while len(stack) > 0:
        another_stack.append(stack.pop())

    stack = another_stack

    print("\nOperation performed: REVERSE STACK")
    display(stack)

    return stack


def main():
    stack = []

    while True:
        print("\nSTACK OPERATIONS")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Reverse String using Stack")
        print("5. Reverse Stack using another Stack")
        print("6. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            push(stack)

        elif choice == 2:
            pop_element(stack)

        elif choice == 3:
            print("\nOperation performed: DISPLAY")
            display(stack)

        elif choice == 4:
            reverse_string()

        elif choice == 5:
            stack = reverse_stack(stack)

        elif choice == 6:
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")


main()
