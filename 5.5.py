def findPeakElement(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return right
peak_index = findPeakElement([5,10,20,15])
print("The peak element is at index", peak_index, "with value", [5,10,20,15][peak_index])

