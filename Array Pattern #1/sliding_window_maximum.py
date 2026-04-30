class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        n = len(nums)
        deque = Deque()
        deque.append(0)
        for i in range(1, k):
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)
        result.append(nums[deque[0]])
        for j in range(k, n):
            start_point = j - k + 1
            while deque and deque[0] < start_point:
                deque.popleft()
            while deque and nums[deque[-1]] < nums[j]:
                deque.pop()
            deque.append(j)
            result.append(nums[deque[0]])
        return result
