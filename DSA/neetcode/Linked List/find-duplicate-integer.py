#copy-paste by ai...
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Phase 1: Detect the intersection point inside the cycle
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]           # moves 1 step
            fast = nums[nums[fast]]     # moves 2 steps
            if slow == fast:
                break

        # Phase 2: Find the entrance to the cycle (the duplicate value)
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]           # moves 1 step
            slow2 = nums[slow2]         # moves 1 step

        return slow