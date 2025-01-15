class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self): # method checks if the stack is empty
        return len(self.stack) == 0

    def push(self, item): # method adds an item to the top of the stack
        self.stack.append(item)

    def pop(self): # method removes the top item from the stack
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self): # method returns the top item from the stack without removing it
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def size(self): # method returns the size of the stack
        return len(self.stack)

# Example usage:
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())  # Output: 3
    print(s.peek())  # Output: 2
    print(s.size())  # Output: 2

# Time complexity of all the methods is O(1) - constant time complexity