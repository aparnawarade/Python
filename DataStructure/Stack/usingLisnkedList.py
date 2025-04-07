#Create a Stack class that represents a last-in, first-out (LIFO) data structure using a linked list implementation.

# class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
    #                               #
    #                               #
    #                               #
    #                               #
    #################################
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
# class Stack:
    ## WRITE STACK CONSTRUCTOR HERE ##
    #                                #
    #                                #
    #                                #
    #                                #
    ##################################

class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1 
        
    def print_stack(self):
        if not new_node:
            return False
        temp=new_node.top
        while temp:
            print(temp.value)
            temp=temp.next
        
"""
Implement the push method for the Stack class that adds a new node with a given value to the top of the stack.

The method should perform the following tasks:

Create a new instance of the Node class using the provided value.

Set the next attribute of the new node to point to the current top node.

Update the top attribute of the Stack class to point to the new node.

Increment the height attribute of the Stack class by 1.
"""
### WRITE PUSH METHOD HERE ###
    #                            #
    #                            #
    #                            #
    #                            #
    ##############################
    def push(self,value):
        new_node=Node(value)
        
        if not self.top:
            self.top = new_node
            self.height = 1
        else:
            new_node.next=self.top
            self.top=new_node
            self.height +=1 
            
### WRITE POP METHOD HERE ###
    #                           #
    #                           #
    #                           #
    #                           #
    #############################
    def pop(self):
        if not self.top:
            return None
        
        temp=self.top
        self.top=self.top.next
        temp.next=None
        self.height -=1 
        return temp
        





my_stack = Stack(2)

print('Top:', my_stack.top.value)
print('Height:', my_stack.height)



"""
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1

"""

print('Stack before push(1):')
my_stack.print_stack()

my_stack.push(1)

print('\nStack after push(1):')
my_stack.print_stack()


#---
print('Stack before pop():')
my_stack.print_stack()

print('\nPopped node:')
print(my_stack.pop().value)

print('\nStack after pop():')
my_stack.print_stack()
