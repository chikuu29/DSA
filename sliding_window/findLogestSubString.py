# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


def findResult(input):
    # print(input)
    hashMap=set()  
    left=0
    lMax=0
    for right in range(len(input)):
        while input[right] in hashMap:
            # print(hashMap)
            hashMap.remove(input[left])
            left+=1
            
        

        hashMap.add(input[right])
        lMax=max(lMax,right-left+1)
        # print(left)
        # lMax=max()
        # print(input[end])
    print(hashMap)
    return lMax


input="abcabcbb"
result=findResult(input)
print(f"Result:",result)