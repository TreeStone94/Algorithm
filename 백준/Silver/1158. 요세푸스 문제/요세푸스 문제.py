n, k = map(int, input().split())

# 1부터 n까지의 사람들을 리스트로 만들기
people = list(range(1, n + 1))
result = []
idx = 0  # 현재 위치

# 모든 사람이 제거될 때까지 반복
while people:
    # k번째 사람의 인덱스 계산 (0-based)
    idx = (idx + k - 1) % len(people)
    # 해당 사람을 제거하고 결과에 추가
    result.append(people.pop(idx))

# 결과 출력
print('<' + ', '.join(map(str, result)) + '>')