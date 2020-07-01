def convert(nums):
    num = 0
    idx = 0
    for i in range(len(nums)-1, -1, -1):
        num += nums[i] * 2**(len(nums)-1-i)
        idx+=1
    return num

print(convert([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]))