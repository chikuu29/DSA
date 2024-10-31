

def findResult(input,k):
    maxSum=0
    sum=0
    start=0
 
    for end in range(len(input)):
        sum+=input[end]
        if end-start+1==k:
            maxSum=max(maxSum,sum)
            sum-=input[start]
            start+=1
    return maxSum

input=[3, 5, 2, 1, 7]
k=4
# Output: 8
result=findResult(input,k)
print(result)