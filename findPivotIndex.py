"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 
"""

def find_left_sum(num,i):
    SUM=0
    for j in range(0,i):
        SUM=SUM+num[j]
    return SUM

def find_right_sum(num,i):
    SUM=0
    for j in range(i+1,len(num)):
        SUM=SUM+num[j]
    return SUM

num=[1,7,3,6,5,6]

for i in range(len(num)):
    left_sum = find_left_sum(num, i)
    right_sum = find_right_sum(num,i)
    if left_sum==right_sum:
        print(i)
            
            
        
#better solution 
total_sum=sum(num)
print(total_sum)
left_sum=0
for i in range(len(num)):
    if left_sum == total_sum-num[i]-left_sum:
        print(i)
    left_sum=left_sum+num[i]

