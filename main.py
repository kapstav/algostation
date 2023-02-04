nums1=input('Enter numbers separated by spaces:').split()
nums2=input('Enter numbers separated by spaces:').split()
def getCommon(nums1, nums2):
 for i in range(len(nums1)):
  if nums1[i] in nums2:
   return nums1[i]
 return -1
print(getCommon(nums1, nums2))