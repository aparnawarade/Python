Most of linked list problem can be solved with two pointers 
E,g 
Fast and slow pointer 
Find middle of linked list (middle will be slow if fast moves with double the speed ) LeetCode #876 
FInd Loop in linked list (traverse till fast==slow) Leetcode #141 | Solution
Two pointers at a distance
Fins Kth node from last (move fast till K and then when fats reaches end ,kth node is slow pointer ) Leetcode #19
Reverse Linked list (prev , curr, next pointer) Leetcode #206
Dummy node 
Meging a linked list (take dummy node and merge to that node baked on value ) Leetcode #21 (dummy node and two pinters at two list )

Pallindrome linked list Leetcode #234
Hint: Use fast and slow pointers to find the middle of the linked list, and reverse the second half of the linked list, and compare the values of the nodes in the first half and the reversed second half.

Reorder list (Leetcode #143)

Hint: Use fast and slow pointers to find the middle of the linked list, reverse the second half of the linked list, and merge the two halves of the linked list together.

When to Use fast and slow pointer (Notes)
Fast and slow pointers is a technique that is used to find the middle node in a linked list. We initialize two pointers, slow and fast, that start at the head of the linked list. We then iterate until fast reaches the end of the list. During each iteration, the slow pointer advances by one node, while the fast pointer advances by two nodes. When the fast pointer reaches tail of the list, the slow pointer points to the middle node.

When to use Dummy node (Notes)
If you find yourself writing a solution where you need to introduce a special case to initialize the head of a linked list, and the logic for handling the head is the same as the logic for handling the rest of the linked list, you should consider using a dummy node to simplify your solution.
Using a dummy node under these conditions involves the following 3 steps:
Creating the dummy node to represent the head of the linked list you are constructing.
Now, you can iteratively append nodes to the end that linked list based on the logic of the problem.
Returning dummy.next as the head of the linked list you constructed.
Other Use Cases
Dummy nodes can also simplify the logic of removing a node in a linked list. As we saw above, removing a node in a linked list requires a reference to the previous node of the node you want to remove. By prepending a dummy node to the head of the link list, we can ensure that each node (including the head) has a previous node, and we can avoid handling the head of the linked list as a special case
Problem on Dummy node 

Swap Nodes in Pairs Leetcode #24 | Solution
Hint: Start by figuring out the pointers you need to manipulate in order to swap two nodes in the middle of a linked list, then think about how using a dummy node can simplify your solution.
Partition List Leetcode #86
Hint: Use two dummy nodes!
The function partition_list takes an integer x as a parameter and modifies the current linked list in place according to the specified criteria. If the linked list is empty (i.e., head is null), the function should return immediately without making any changes.
Example 1:
Input:
Linked List: 3 -> 8 -> 5 -> 10 -> 2 -> 1 x: 5
Process:
Values less than 5: 3, 2, 1
Values greater than or equal to 5: 8, 5, 10
Output:
Linked List: 3 -> 2 -> 1 -> 8 -> 5 -> 10


Remove Nth Node From End of List Leetcode #19 | Solution
Hint: Use a dummy node to avoid handling the case of removing the head of the linked list as a special case.
Remove Duplicates (Leetcode #83 )
Reverse Sublist ( Leetcode 92)
