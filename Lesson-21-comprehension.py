numbers = [1000, 2000, 3000, 4000]
double_price = []
for number in numbers :
    double_price.append(number*2)
print(double_price)
double_price = [number*2 for number in numbers]
print(double_price)



nums = [1,2,3,4,5,6,7,8,9]
double_num = [num*2 for num in nums if (num%2) == 0]
print(double_num)
