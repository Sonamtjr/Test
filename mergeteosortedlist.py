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

    def print_list(self):
        """Print all nodes in the list."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")  # Indicate the end of the list

    @staticmethod
    def merge_sorted_lists(list1, list2):
        """Merge two sorted linked lists into one sorted linked list."""
        dummy = Node()  # Dummy node to simplify the merging process
        tail = dummy

        current1 = list1.head
        current2 = list2.head

        while current1 and current2:
            if current1.data < current2.data:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            tail = tail.next

        # Attach the remaining elements
        if current1:
            tail.next = current1
        elif current2:
            tail.next = current2

        # Create a new LinkedList for the merged result
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list
if __name__ == "__main__":
    # Create first sorted linked list
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)

    # Create second sorted linked list
    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)

    # Print the original lists
    print("List 1:")
    list1.print_list()
    print("List 2:")
    list2.print_list()

    # Merge the two sorted linked lists
    merged_list = LinkedList.merge_sorted_lists(list1, list2)

    # Print the merged list
    print("Merged list:")
    merged_list.print_list()
