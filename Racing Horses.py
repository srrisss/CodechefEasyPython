t = int(input())
while t :
    t -= 1
    n = int(input())
    nums = input().split()
    nums = list(map(int, nums))
    nums.sort()
    a = []
    for i  in range(0,n-1) :
        a.append(nums[i+1] - nums[i])
    print(min(a))
