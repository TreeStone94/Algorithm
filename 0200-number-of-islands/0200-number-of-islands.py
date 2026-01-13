class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 상,하,좌,우에 섬이 있는가?
        rows = len(grid)
        cols = len(grid[0])
        
        island = 0
        def find_island(r,c):

            # 0을 만나거나, 밖으로 빠지거나, rows,cols가 같아졌을때 멈춤
            if r < 0 or c < 0 or r >= rows  or c >= cols or grid[r][c] == "0":
                return
            # 방문한 island는 0으로 처리
            grid[r][c] = "0"

            # 상,하,좌,우 이동
            find_island(r-1,c) # 상
            find_island(r+1,c) # 하
            find_island(r,c-1) # 좌
            find_island(r,c+1) # 우

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island +=1
                    find_island(r,c)
        return island



        