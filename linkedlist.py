class Node:
    def __init__(self, data=None):
        self.data = data  # Data held by the node
        self.next = None  # Reference to the next node in the list
class LinkedList:
    def __init__(self):
        self.head = None  # Head of the list

    def append(self, data):
        """Append a node with the given data to the end of the list."""
        new_node = Node(data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, set the new node as the head
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next  # Traverse to the end of the list
        last_node.next = new_node  # Set the next reference of the last node to the new node

    def prepend(self, data):
        """Prepend a node with the given data to the start of the list."""
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Set the next reference of the new node to the current head
        self.head = new_node  # Set the new node as the head

    def delete_with_value(self, data):
        """Delete the first node that contains the given data."""
        if self.head is None:
            return  # If the list is empty, do nothing
        if self.head.data == data:
            self.head = self.head.next  # If the head contains the data, remove the head
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next  # Bypass the node to be deleted
                return
            current_node = current_node.next

    def find(self, data):
        """Find if a node with the given data exists in the list."""
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True  # Return True if data is found
            current_node = current_node.next
        return False  # Return False if data is not found

    def print_list(self):
        """Print all nodes in the list."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")  # Indicate the end of the list
if __name__ == "__main__":
    # Create a new LinkedList
    linked_list = LinkedList()

    # Append elements
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    # Prepend element
    linked_list.prepend(0)

    # Print the list
    linked_list.print_list()

    # Find an element
    print(linked_list.find(2))  # Output: True
    print(linked_list.find(5))  # Output: False

    # Delete an element
    linked_list.delete_with_value(2)

    # Print the list again
    linked_list.print_list()