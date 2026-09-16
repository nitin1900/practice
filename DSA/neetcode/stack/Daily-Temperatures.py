#my code... solved myself but used ai to decompose or debug the errors..
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for idx, temp in enumerate(temperatures):
            days = 0
            for j in range(idx + 1, len(temperatures)):
                if temperatures[j] > temp:
                    days = j - idx
                    break
            result.append(days)
        return result


#solution optimized...
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = i - prev_day
            stack.append(i)
        return result
