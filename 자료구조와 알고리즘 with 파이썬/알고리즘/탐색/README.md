## 탐색이란?

데이터의 집합에서 원하는 조건을 만족하는 데이터를 찾는 작업

## 순차 탐색
 
데이터 중에서 원하는 키값을 가진 레코드를 처음부터 하나씩 순서대로 검사하여 찾는 알고리즘

```python
def sequential_search(A, key, low, high):
	for i in range(low, high+1)
		if A[i] == key:
			return i
	return -1
```

### 순차 탐색의 특징

- 탐색의 정의를 직접 사용하는 알고리즘
- 시간복잡도가 O(n)이라 효율적이지 않음
- 데이터가 정렬되어 있지 않다면 순차 탐색 이외에 별다른 대안 없음

### 순차 탐색 개선 방법

레코드 중에서 자주 검색되는 것들을 가능한 앞에 두는 것(자기 구성 순차 탐색)

- 맨 앞으로 보내기
    
    탐색에 성공한 레코드를 리스트의 맨 앞으로 보내는 방법, 한번 탐색된 레코드가 바로 이어서 다시 탐색될 가능성이 많을때 사용
    
- 교환하기
    
    바로 앞의 레코드와 교환(점진적 이동)
    
    ```python
    def sequential_search_transponse(A, key, low, high):
    	for i in range(low, high+1):
    		if A[i] == key:
    			if i > low:
    				A[i], A[i-1] = A[i-1], A[i]
    				i = i-1
    			return i
    		return -1
    ```
    
## 이진 탐색

한 번 비교할 때마다 탐색 범위가 절반으로 줄어들기 때문에 ‘이진’이라 부름

데이터가 키값 기준에서 정렬되어 있을 때 이진 탐색 알고리즘이 효율적

```python
# 순환 구조
def binary_search(A, key, low, high):
	if (low <= high):
		middle = (low + high)//2
		if key == A[middle]:
			return middle
		elif (key < A[middle]):
			return binary_search(A, key, low, middle-1)
		else:
			return binary_search(A, key, middle + 1, high)
	return -1
	
# 반복 구조
def binary_search_iter(A, key, low, high):
	while (low <= high):
		middle = (low + high) // 2
		if key = A[middle]:
			return middle
		else (low < A[middle]):
			high = middle -1
		else:
			low = middle + 1
	return -1
```

### 이진 탐색의 특징

- 시간복잡도가 ○(log₂n)인 매우 효율적인 탐색 방법
- 반드시 배열이 정렬되어 있어야 사용 가능
- 데이터가 한번 만들어지면 이후로 변경되지 않고 탐색 연산만 처리한다면 이진 탐색이 최고의 선택 중 하나
- 데이터의 삽입이나 삭제가 빈번한 응용에는 이진 탐색이 비효율적

### 보간 탐색

탐색 키가 존재할 위치를 예측하여 탐색하는 방법

탐색 범위 가장자리(low, high)에 있는 데이터의 키값과 탐색 키의 비율을 고려하여 위치를 계산

이진 탐색 함수에서 middle 계산만 다음과 같이 수정하면 됨

```python
middle = int(low+ (high-low)* (key-A[low]) / (A[high]-A[low[))
```
