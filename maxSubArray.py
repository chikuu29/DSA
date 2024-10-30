# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def maxSubArray(n,target):
    hashMap={}
    print(n)
    for i,num in enumerate(n):
        # print(i)
        # print(num)
        diff=target-num
        # print(diff)
        # print(hashMap)
        if diff in hashMap:
            # print(diff)
            return [hashMap[diff], i]

        else:
            hashMap[num] = i

        
        print(hashMap)
        # for j in range(i+1,len(n)):
        #     print(f'({n[i],n[j]})')
        #     if n[i]+n[j]==target:
        #         result.append(i)
        #         result.append(j)

            # print(f"({n[i:j+1]})")


a =[2,7,11,15]
# a=[3,2,4]
# a=[3,3]
result=maxSubArray(a,target=9)



print("result",result)

