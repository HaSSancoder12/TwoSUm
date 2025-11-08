num=[24,64,98,78]
target=102
def twoSum(num,target):
    dic={}
    for i,num in enumerate (num):
        if target-num in dic:
            return [dic[target-num],i]
        dic[num]=i

    return[]

print(twoSum(num,target))
