#给定一个整数数组nums和一个整数目标值 target,请你在该数组中找出 
#和为目标值 target 的那两个整数，并返回它们的数组下标。
#你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#你可以按任意顺序返回答案

class Solution:
    def twoSum (self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
                

def main():
    nums=[2,7,11,15]
    target=9
    print(Solution().twoSum(nums,target))