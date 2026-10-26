class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        q = deque()

        for r in range(rows):
            for c in range(cols): 
                if grid[r][c] == 2:
                    q.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1
        
        def visitNeighbor(r,c):
            nonlocal fresh
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return
            else:
                grid[r][c] = 2
                fresh -= 1
                q.append([r,c])

        minutes = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == 2:
                    visitNeighbor(r+1, c)
                    visitNeighbor(r-1, c)
                    visitNeighbor(r, c+1)
                    visitNeighbor(r, c-1)

            minutes += 1

        return minutes if fresh == 0 else -1
            

        