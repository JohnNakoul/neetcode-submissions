class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            previous = ans[-1]

            if previous[1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                previous[1] = max(previous[1], intervals[i][1])

        return ans
