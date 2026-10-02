class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in temperatures]

        for i in reversed(range(0, len(res) - 1)):
            j = i + 1
            while j < len(res):
                if temperatures[i] < temperatures[j]:
                    res[i] = j - i
                    break
                elif res[j] == 0:
                    res[i] = 0
                    break
                else:
                    j = j + res[j]

        return res