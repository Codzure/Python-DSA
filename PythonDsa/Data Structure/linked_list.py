from typing import List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_linked_list(self): 
        temp = self.head  # Start traversal from the head of the linked list.
        while temp is not None:  # Continue until the end of the linked list (where temp becomes None).
            print(temp.value)  # Print the value of the current node.
            temp = temp.next  # Move to the next node.

            # Traversing means going through every single node, starting with the head of the linked list 
            # and ending on the node that has a next value of None.
            # In the print_linked_list method, we start traversing from the head of the linked list.
            # We print the value of the current node and move to the next node.
            # We continue this process until we reach the end of the linked list.
            # This way, we can print all the values of the linked list.
            # This is the basic idea of traversing a linked list.


  
    def append(self, value):
        new_node = Node(value) # Create a new node with the given value

        if self.head is None:
            self.head = new_node  # Set the new node as the head
            self.tail = new_node  # Set the new node as the tail (since it's the only node)
        else:
            self.tail.next = new_node  # Link the current tail to the new node
            self.tail = new_node       # Update the tail to be the new node

        self.length += 1
        return True
    
            # The append method adds a new node to the end of the linked list.
            # It takes a value as an argument and creates a new node with that value.
            # If the linked list is empty, it sets the new node as both the head and the tail.
            # If the linked list is not empty, it links the current tail to the new node and updates the tail to be the new node.
            # Finally, it increments the length of the linked list and returns True to indicate that the operation was successful.
            # This method has a time complexity of O(1) because it always adds a new node at the end of the linked list in constant time.
            
    def prepend(self, value):
        new_node = Node(value)  # Create a new node with the given value

        if self.head is None: # or if self.length == 0 ~ If the linked list is empty
            self.head = new_node  # Set the new node as the head
            self.tail = new_node  # Set the new node as the tail (since it's the only node)
        else:
            new_node.next = self.head  # Link the new node to the current head
            self.head = new_node       # Set the new node as the head

        self.length += 1
        return True
    
             # The prepend method adds a new node to the beginning of the linked list.

    def pop(self, value): 
        
        if self.head is None:
            return None

        temp = self.head
        pre = self.head

        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        pre.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp
    
            # The pop method removes the last node from the linked list.
            # It returns the removed node or None if the linked list is empty.
            # The method starts by checking if the linked list is empty and returns None if it is.
            # It then traverses the linked list to find the second-to-last node (pre) and the last node (temp).
            # It updates the tail to be the second-to-last node (pre) and removes the link to the last node.
            # The method decrements the length of the linked list and handles the case where the linked list becomes empty.
            # Finally, it returns the removed node.
            # This method has a time complexity of O(n) because it traverses the entire linked list to find the last node.
            # The space complexity is O(1) because it uses a constant amount of extra space regardless of the size of the linked list.      

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.pop(5)
my_linked_list.prepend(10) # 


my_linked_list.print_linked_list()