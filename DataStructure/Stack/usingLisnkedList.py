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
        


my_stack = Stack(4)

print('Top:', my_stack.top.value)
print('Height:', my_stack.height)



"""
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1

"""
