
def result(array,number):

    length=len(array)-1
    left=0
    right=length
    while right>=left:
        mid=(right+left)//2
        print(mid)
        if number==array[mid]:
            return mid
        elif array[mid]>number:
            right=mid-1
        else:
            left=mid+1
    return -1


        




array=[1,3,5,7,8,9,10,20,21,22]
print(result(array,20))