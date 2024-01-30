nums= [50, 35, 78, 66, 17]
#output [17, 66, 78, 35, 50]


left =0
right=len(nums)-1

while left<right :
    nums[left],nums[right],left,right=nums[right],nums[left],left+1,right-1

print(nums)
