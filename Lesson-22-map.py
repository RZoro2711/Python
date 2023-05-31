nums = [1,2,3,4,5,6,7,8,9]
def mapfun(num) :
    return num * 2
print(list(map(mapfun, nums)))


ans = [num*2 for num in nums]
print(ans)