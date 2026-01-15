def solution(m, n, puddles):
    answer = 0
    MOD = 1_000_000_007
    # 1. DP 테이블 초기화
    dp = [[0 for _ in range(m)] for _ in range(n)]
    

    # 2. 물웅덩이 처리
    puddle_set = set((p[1]-1, p[0]-1) for p in puddles)
    # 3. 시작점 초기화
    dp[0][0] = 1
     # 4. 첫 행 초기화 (오른쪽으로만 이동)
    for j in range(1, m):
          if (0, j) not in puddle_set:
                dp[0][j] = dp[0][j-1]
          # 물웅덩이면 0 유지

      # 5. 첫 열 초기화 (아래로만 이동)
    for i in range(1, n):
          if (i, 0) not in puddle_set:
                dp[i][0] = dp[i-1][0]
    # 4. DP 테이블 채우기
    for i in range(1, n):
          for j in range(1, m):
              # 현재 위치가 물웅덩이면 건너뛰기
              if (i, j) in puddle_set:
                    continue

              # 점화식 적용
              dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

    # 5. 결과 반환
    
    return dp[n-1][m-1]