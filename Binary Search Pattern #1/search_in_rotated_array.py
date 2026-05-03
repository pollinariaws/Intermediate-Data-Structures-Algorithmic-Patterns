class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start= 0
        end = len(nums) - 1
        ans = -1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] >= nums[0] and target < nums[0]:
                start = mid + 1
            elif nums[mid] < nums[0] and target >= nums[0]:
                end = mid - 1
            else:
                if nums[mid] < target:
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    ans = mid
                    break
        return ans
