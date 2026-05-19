#
# table des matiere
# 1 Minimum Common Value
# 2 Two Sum
# 
# 
# 
# 
# 
# 
# 
#  Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

 

# Example 1:

# Input: nums1 = [1,2,3], nums2 = [2,4]
# Output: 2
# Explanation: The smallest element common to both arrays is 2, so we return 2.

# Example 2:

# Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
# Output: 2
# Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.

# nums = [1,2,3,6]
# nums2 = [2,3,4,5]

# numscommun = []
# for i in nums2:
#     if i in nums:
#         numscommun.append(i)

# numscommun.sort()
# print(numscommun[0])

# -------------------------------------------------------------------------------------------------------------
# 2. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# nums = [2,7,11,15]
# target = 9
# def twoSum(nums, target):
#     for i in range(0, len(nums)):
#         for j in range(0, len(nums)):
#             if nums[i] != nums[j] and nums[i] + nums[j]==target:
#                 return(i, j)

# -------------------------------------------------------------------------------------------------------------
# Roman to Integer

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

#     I can be placed before V (5) and X (10) to make 4 and 9. 
#     X can be placed before L (50) and C (100) to make 40 and 90. 
#     C can be placed before D (500) and M (1000) to make 400 and 900.

# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4

# def RomanToInteger(texte):
#     texte.upper()
#     reponse = 0
#     for i in range(0, len(texte)):
         
#             match texte[i]:
#                 case "M":
#                     reponse += 1000
#                 case "D":
#                     reponse += 500
#                 case "C" :
#                     reponse += 100
#                 case "L" :
#                     reponse += 50
#                 case "X" : 
#                     reponse += 10
#                 case "V" :
#                     reponse += 5
#                 case "I" : 
#                     reponse += 1
#     print(reponse)
# texte = "LVIII"
# RomanToInteger(texte)



# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

