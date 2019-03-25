# def findTargetSumWay(nums,s):
#     if len(nums) == 0:
#         return 0
#     memo = {}
#     return dfs(0,0,nums,s,memo)
#
# def dfs(startIndex,curSum,nums,target,memo):
#     if (startIndex, target-curSum) in memo:
#         print({"memo: ": memo[(startIndex,target - curSum)]},{"startIndex": startIndex},{"target-curSum": target-curSum})
#         return memo[(startIndex,target - curSum)]
#
#     if startIndex == len(nums):
#         print("*******> ")
#         print({"StartIndex": startIndex},{"len(nums)": len(nums)},{"curSum": curSum})
#         if curSum == target:
#             print({"Cur Sum and Target Same": curSum})
#             return 1
#         return 0
#
#     ways = 0
#     print({"first dfs":curSum},{"way": ways},{"memo": memo},{"startIndex": startIndex})
#     ways += dfs(startIndex+1,curSum+nums[startIndex],nums,target,memo)
#     print({"second dfs": curSum},{"ways": ways},{"memo": memo},{"startIndex": startIndex})
#     ways += dfs(startIndex+1,curSum-nums[startIndex],nums,target,memo)
#     print({"ways!!!": ways})
#     memo[(startIndex,target-curSum)] = ways
#     return ways

def findTargetSumWay(nums,s):
    if len(nums) == 0:
        return 0
    total = sum(nums)
    #print({"Total": total})
    return helper(nums,s,0,total);

def helper(nums,s,index,total):
    #print({"nums": nums},{"Total": total},{"index": s})
    if index == len(nums):
        if s == 0:
            return 1;
        return 0

    ways = 0;
    ways += helper(nums,s + nums[index],index+1,total-nums[index])
    ways += helper(nums,s - nums[index],index+1,total-nums[index])
    #print({"Ways": ways})
    return ways;






array = [1,1,1,1,1]
target = 3
print(findTargetSumWay(array,target))