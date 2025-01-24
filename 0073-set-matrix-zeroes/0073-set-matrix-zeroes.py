class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        
        # 첫 번째 스캔: 0을 발견하면 임시 값 -1로 바꾸기
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    # 해당 행과 열의 모든 값을 임시로 -1로 변경
                    for i in range(rows):  # 해당 열의 모든 값
                        if matrix[i][c] != 0:
                            matrix[i][c] = -1
                    for j in range(cols):  # 해당 행의 모든 값
                        if matrix[r][j] != 0:
                            matrix[r][j] = -1
        
        # 두 번째 스캔: 임시 값 -1을 최종적으로 0으로 변환
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == -1:
                    matrix[r][c] = 0

                