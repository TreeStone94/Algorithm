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
