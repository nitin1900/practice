#copy-paste code from ai...
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # stores indices of elements in nums
        l = 0

        for r in range(len(nums)):
            # Maintain monotonic property: remove smaller values from the back
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Remove index from front if it falls outside the current window
            if l > q[0]:
                q.popleft()

            # Window has reached size k, record the maximum (always at q[0])
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

        return output