def merge(nums1, m, nums2, n):
    # p1 = m - 1  # pointer for nums1 2
    # p2 = n - 1  # pointer for nums2 2
    # p = m + n - 1  # pointer for the merged array 5
    #
    # # Continue until we have considered all elements of nums2
    # while p1 >= 0 and p2 >= 0:
    #     if nums1[p1] > nums2[p2]:
    #         nums1[p] = nums1[p1]
    #         p1 -= 1
    #     else:
    #         nums1[p] = nums2[p2]
    #         p2 -= 1
    #     p -= 1
    #
    # # If there are still elements in nums2, copy them into nums1
    # while p2 >= 0:
    #     nums1[p] = nums2[p2]
    #     p2 -= 1
    #     p -= 1
    start = m
    for val in nums2:
        nums1[start] = val
        start += 1
    return nums1.sort()


# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
