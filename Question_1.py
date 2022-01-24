nums = [2,11,15,3,4,5,7]
target = 26
from itertools import product
tup_lis = list(product(nums,nums))
result = []
for pair in tup_lis:
    if pair[0] != pair[1]:
        if sum(pair) == target:
            result.append(nums.index(pair[0]))
            result.append(nums.index(pair[1]))
            break
print(result)