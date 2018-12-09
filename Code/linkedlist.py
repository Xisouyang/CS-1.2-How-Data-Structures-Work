#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0     # Keep track of size of linked-list

        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?

        Best and Worst case: O(1) - This implementation increments size property
        each time an element is added. Thus, this function simply needs to return
        that property - 1 operation
        """
        # TODO: Loop through all nodes and count one for each

        return self.size            # Returns the length of linked-list(size == length)

        # length = 0                # initialize variable to store length
        # node = self.head          # Start at the head of linked-list(just accessing our list)
        # while node is not None:   # Iterate through the nodes of the linked-list
        #     length += 1           # increment length
        #     node = node.next      # go to next node
        # return length             # Return the length of the list
        # return self.size          # Same^

    def append(self, item):
        """Insert the given item at the tail of this linked list.

        TODO: Running time: O(???) Why and under what conditions?

        Best and Worst case: O(1) - This linkedlist implementation has tail property,
        so this function simply adds a new node after the tail, and updates the tail pointer.

        """
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists

        assert item is not None         # Checks to see if item exists
        new_node = Node(item)           # Creates the item

        if self.is_empty():             # if the linked-list is empty
            self.head = new_node        # set new node as head
            self.tail = new_node        # new node is also the tail if its the first item in list
        else:
            # node = self.head          # Access linked-list through the head
            # while node.next != None:  # Checks for empty list
            #     node = node.next      # go to next node in list
            # node.next = new_node      # insert new node
            # self.tail = new_node      # set tail to the new end of the list

            self.tail.next = new_node   # insert new node at end of the list
            self.tail = new_node        # set tail as the end of the list
        self.size += 1                  # increment size each time new node is added to list


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?

        Best and Worst case: O(1) - Same algorithm as append function,
        but instead of looking at the tail property we look at the head.
        """
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists

        assert item is not None         # Checks for existing item
        new_node = Node(item)           # Create new node

        if self.is_empty():             # if our list is empty
            self.head = new_node        # new node is start of our list
            self.tail = new_node        # if list is empty first item is also the tail
        else:
            new_node.next = self.head   # prepend new node to list
            self.head = new_node        # set head to the new front of list

        self.size += 1                  # increment size

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?

        Best Case: O(1) - find item at or near head, few to 1 operation
        Worst Case: O(n) - item is close to or at the end or does not exist in
        list - must traverse through entire list - n operations

        """
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function

        node = self.head                # Access linked-list through the head
        while node != None:             # Iterate through list
            item = node.data            # Assign node data to a variable
            if quality(item) == True:   # Checks to see if node data matches with desired item
                return item             # If true return item
            node = node.next            # If not move on to next node
        return None                     # If item not in list return none

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.

        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?

        Best Case: O(1) - find item at the head and delete, only do 1 operation
        Worst Case: O(n) - item does not exist in the linked-list, and goes through
        entire list to try - takes n operations

        """
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

        if self.is_empty():                             # Checks to see if linked-list is empty
            raise ValueError("Item not found: {}.".format(item))

        if self.size == 1:                              # Checks to see if there's only one node in list

            # delete that single node from list, update length
            self.head = None
            self.tail = None
            self.size -= 1
            return True

        prev_node = None                                # initialize a pointer to the node before the current
        curr_node = self.head                           # initialize pointer to the head to access the linked-list

        while curr_node:                                # Iterate through the linked-list
            if curr_node.data == item:                  # If the item is found
                if curr_node == self.tail:              # Check to see if the data is associated w/ the last node
                    prev_node.next = None               # discard the node w/ that data
                    self.tail = prev_node               # reset tail to point to the new last node
                    self.size -= 1                      # update length of the linked-list
                    return True                         # Yes we deleted successfully
                if prev_node:                           # If the node associated w/ data is somewhere in the middle
                    prev_node.next = curr_node.next     # discard node w/ data by switching pointers
                    self.size -= 1                      # update size
                else:                                   # node w/ data is the head
                    self.head = curr_node.next          # discard node w/ data
                    self.size -= 1                      # update length
                return True

            prev_node = curr_node                       # update previous node to point to the next node
            curr_node = curr_node.next                  # update current node to point to the next node

        raise ValueError("Item not found: {}.".format(item))    # Did not find item

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    ll.append(None)
    print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    another = ['D']
    ll.prepend(another[0])
    print('list: {}'.format(ll))
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))

if __name__ == '__main__':
    test_linked_list()
