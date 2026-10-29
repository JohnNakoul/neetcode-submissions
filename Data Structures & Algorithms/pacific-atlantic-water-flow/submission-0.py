class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        ans = []

        def dfs(r, c, visited, prev):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or heights[r][c] < prev:
                return

            else:
                visited.add((r,c))
                dfs(r+1,c,visited,heights[r][c])
                dfs(r-1,c,visited,heights[r][c])
                dfs(r,c+1,visited,heights[r][c])
                dfs(r,c-1,visited,heights[r][c])

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])

        for i in range(rows):
            for j in range(cols):
                if (i,j) in atlantic and (i,j) in pacific:
                    ans.append([i,j])
        return ans
