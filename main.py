'''
nums1=input('Enter numbers separated by spaces:').split()
nums2=input('Enter numbers separated by spaces:').split()
def getCommon(nums1, nums2):
 for i in range(len(nums1)):
  if nums1[i] in nums2:
   return nums1[i]
 return -1
print(getCommon(nums1, nums2))
#-----------------------
var1=[7,8,9,10]
if 9 in var1:
  print('ahha')
#--------------------
numbers = [{"value": 3}, {"value": 1}, {"value": 4}]
numbers = sorted(numbers, key=lambda x: x["value"])
print(numbers)  # Output: [{"value": 1}, {"value": 3}, {"value": 4}]
numbers = [5,7,9,3]
numbers = sorted(numbers, key=lambda x: x)
print(numbers)  # Output: [{"value": 1}, {"value": 3}, {"value": 4}]


import math


class redwick:

  def isReachable(self, x: int, y: int) -> bool:
    a = math.gcd(x, y)
    while a % 2 == 0:
      a //= 2
    return a == 1


p = redwick()
print(p.isReachable(64, 71))

'''


class Solution:

  def getCommon(self,nums1,nums2):
    if(len(nums1)==0): return -1
    elif(len(nums1)==0):pass
    else:
    
      nums1.sort()
      nums2.sort()

      for i in range(len(nums2)):
        if (nums1[i] in nums2):
          return nums1[i]
      return -1

p=Solution()
print(p.getCommon([1,2,3,4],[8,3,4,5]))
print(p.getCommon([],[8,3,4,5]))
 