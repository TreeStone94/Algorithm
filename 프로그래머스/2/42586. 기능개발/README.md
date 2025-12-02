# [level 2] 기능개발 - 42586 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42586) 

### 성능 요약

메모리: 9.24 MB, 시간: 0.08 ms

### 구분

코딩테스트 연습 > 스택／큐

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 12월 02일 19:17:53

### 문제 설명

<p>프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.</p>

<p>또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.</p>

<p>먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.</p>

<h5>제한 사항</h5>

<ul>
<li>작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.</li>
<li>작업 진도는 100 미만의 자연수입니다.</li>
<li>작업 속도는 100 이하의 자연수입니다.</li>
<li>배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>progresses</th>
<th>speeds</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[93, 30, 55]</td>
<td>[1, 30, 5]</td>
<td>[2, 1]</td>
</tr>
<tr>
<td>[95, 90, 99, 99, 80, 99]</td>
<td>[1, 1, 1, 1, 1, 1]</td>
<td>[1, 3, 2]</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
첫 번째 기능은 93% 완료되어 있고 하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능합니다.<br>
두 번째 기능은 30%가 완료되어 있고 하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능합니다. 하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 첫 번째 기능이 배포되는 7일째 배포됩니다.<br>
세 번째 기능은 55%가 완료되어 있고 하루에 5%씩 작업이 가능하므로 9일간 작업 후 배포가 가능합니다. </p>

<p>따라서 7일째에 2개의 기능, 9일째에 1개의 기능이 배포됩니다.</p>

<p>입출력 예 #2<br>
모든 기능이 하루에 1%씩 작업이 가능하므로, 작업이 끝나기까지 남은 일수는 각각 5일, 10일, 1일, 1일, 20일, 1일입니다. 어떤 기능이 먼저 완성되었더라도 앞에 있는 모든 기능이 완성되지 않으면 배포가 불가능합니다.</p>

<p>따라서 5일째에 1개의 기능, 10일째에 3개의 기능, 20일째에 2개의 기능이 배포됩니다.</p>

<p>※ 공지 - 2020년 7월 14일 테스트케이스가 추가되었습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

---

## 풀이 방법

### 1. 초기 접근 방식 (역순 Pop 방식)

**아이디어:**
- `progresses`와 `speeds`를 역순으로 처리 (`pop()`으로 뒤에서부터 꺼냄)
- 작업 완료 일수를 계산하여 `days` 리스트에 저장
- `days` 리스트를 다시 pop하면서 배포 카운트 계산

**코드:**
```python
def solution(progresses, speeds):
    answer = []
    
    # 작업 일자 계산 (역순)
    days = []
    while progresses:
        progress = progresses.pop()
        speed = speeds.pop()
        remain_progress = 100 - progress
        day = remain_progress // speed
        if remain_progress % speed != 0:
            day += 1
        days.append(day)
    
    # 배포 카운트 계산
    count = 0
    while days:
        day = days.pop()
        count += 1
        while days and day >= days[-1]:
            days.pop()
            count += 1
        answer.append(count)
        count = 0
    
    return answer
```

**문제점:**
- **순서 역전**: 배포는 앞에서부터 이루어지는데 역순으로 처리
- **비효율적**: `pop()` 연산이 많아 메모리 재할당 비용 발생
- **가독성**: 로직이 직관적이지 않음

---

### 2. 개선된 방식 (큐 방식) ✅

**아이디어:**
- 작업 일수를 **순서대로** 계산
- 큐(deque)를 사용하여 **앞에서부터** 순차적으로 처리
- 현재 배포일에 함께 배포 가능한 기능들을 카운트

**코드:**
```python
from collections import deque

def solution(progresses, speeds):
    # 작업 일수 계산 (순서대로)
    days = deque()
    for progress, speed in zip(progresses, speeds):
        remain_progress = 100 - progress
        day = remain_progress // speed
        if remain_progress % speed != 0:
            day += 1
        days.append(day)
    
    answer = []
    while days:
        current = days.popleft()  # 앞에서부터 꺼냄
        count = 1
        
        # 현재 배포일에 함께 배포 가능한 기능들
        while days and current >= days[0]:
            days.popleft()
            count += 1
        
        answer.append(count)
    
    return answer
```

**장점:**
- **순서 보장**: FIFO(선입선출) 구조로 문제의 요구사항과 일치
- **효율성**: `popleft()`로 앞에서부터 제거하므로 직관적
- **가독성**: 배포 순서가 명확하게 드러남

---

### 3. 인덱스 방식 (메모리 최적화) ✅

**아이디어:**
- Pop 연산 없이 인덱스만 증가시켜 순회
- 메모리 재할당 비용 제로

**코드:**
```python
def solution(progresses, speeds):
    # 작업 일수 계산
    days = []
    for progress, speed in zip(progresses, speeds):
        remain_progress = 100 - progress
        day = remain_progress // speed
        if remain_progress % speed != 0:
            day += 1
        days.append(day)
    
    answer = []
    i = 0
    while i < len(days):
        current = days[i]
        count = 1
        i += 1
        
        # 현재 배포일에 함께 배포 가능한 기능들
        while i < len(days) and current >= days[i]:
            count += 1
            i += 1
        
        answer.append(count)
    
    return answer
```

**장점:**
- **최고 효율**: Pop 연산 없이 인덱스만 증가
- **간결함**: Import 없이 구현 가능
- **성능**: O(n) 시간복잡도, 메모리 재할당 없음

---

## 핵심 개념

### 올림 계산 방법
```python
# 방법 1: 나머지 확인 (명확함)
day = remain_progress // speed
if remain_progress % speed != 0:
    day += 1

# 방법 2: 음수 트릭 (간결함)
day = -(-(remain_progress // speed))

# 방법 3: math.ceil (가독성 최고)
import math
day = math.ceil(remain_progress / speed)
```

### zip() 함수
두 리스트를 동시에 순회:
```python
for progress, speed in zip(progresses, speeds):
    # progresses[i]와 speeds[i]를 동시에 처리
```

### 큐(Queue) vs 스택(Stack)
- **큐**: FIFO (선입선출) → 순서대로 처리하는 문제
- **스택**: LIFO (후입선출) → 역순 처리하는 문제

---

## 배운 점

1. **문제의 순서성 파악**: "앞에서부터 배포" → 큐 또는 인덱스 순회
2. **자료구조 선택**: 순서가 중요한 문제는 큐(deque) 활용
3. **효율성 고려**: 불필요한 pop 연산 줄이기
