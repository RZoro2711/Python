nums = [1,2,3,4,5,6,7,8,9]
def filter_fun(num) : 
    return num%2 == 0
ans = list(filter(filter_fun, nums))
print(ans)

answer = list(filter(lambda num : (num%2) == 0, nums))
print(answer)