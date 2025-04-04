Leetcode examples 

DLL: Reverse ( ** Interview Question)
Create a new method called reverse that reverses the order of the nodes in the list, i.e., the first node becomes the last node, the second node becomes the second-to-last node, and so on.

To do this, you'll need to traverse the list and change the direction of the pointers between the nodes so that they point in the opposite direction.

Do not change the value of any of the nodes.

Once you've done this for all nodes, you'll also need to update the head and tail pointers to reflect the new order of the nodes.


Pseudo code for the reverse method:

Set current_node to head

While current_node is not None:

Set a temporary variable, temp_next, to current_node.next

Set current_node.next to current_node.prev

Set current_node.prev to temp_next

Set current_node to temp_next (which is actually the previous node after swapping)

Swap head and tail pointers of the DoublyLinkedList


def reverse(self):
        curr=self.head
        
        while curr:
            after=curr.next
            curr.next=curr.prev
            curr.prev=after
            curr=after
        
        self.head,self.tail=self.tail,self.head

is is_palindrome 


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    # WRITE IS_PALINDROME METHOD HERE #
    #                                 #
    #                                 #
    #                                 #
    #                                 #
    ###################################
    def is_palindrome(self):
         # 1. If the length of the doubly linked list is 0 or 1, then 
    # the list is trivially a palindrome. 
        if self.length<=1:
            return True
        else:
            temp1=self.head
            temp2=self.tail
            i=0
            # 3. Traverse through the first half of the list. We only need to 
    # check half because we're comparing two nodes at once: one from 
    # the beginning and one from the end.
            while i<=(self.length-1)/2:
                if temp1.value!=temp2.value:
                    return False
                i+=1 
                temp1=temp1.next
                temp2=temp2.prev
            return True
                
            



my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(2)
my_dll_1.append(1)

print('my_dll_1 is_palindrome:')
print( my_dll_1.is_palindrome() )


my_dll_2 = DoublyLinkedList(1)
my_dll_2.append(2)
my_dll_2.append(3)

print('\nmy_dll_2 is_palindrome:')
print( my_dll_2.is_palindrome() )



"""
    EXPECTED OUTPUT:
    ----------------
    my_dll_1 is_palindrome:
    True

    my_dll_2 is_palindrome:
    False

"""


            
