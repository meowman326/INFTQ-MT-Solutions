n = int(input())
lis = [input() for x in range(n*2)]
students = [ (lis[x],lis[x+1]) for x in range(0,len(lis)-1,2)]
nums = [ele[1] for ele in students]
second_min = sorted(set(nums))[1]
result = [ele[0] for ele in students if ele[1]==second_min]
result.sort()
print(*result,sep='\n')