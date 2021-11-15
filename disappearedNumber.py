def getDisappearedNumbers(arr):
    result = []
    for i in range(1, len(arr) + 1):
        if i not in arr:
            result.append(i)

    return result


nums1 = [4,3,2,7,8,2,3,1]
print(getDisappearedNumbers(nums1))
nums2 = [1,1]
print(getDisappearedNumbers(nums2))
