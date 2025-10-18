## 정렬이란

정렬은 순서대로 나열하는 것을 말합니다. 정렬을 위해서는 서로 비교할 수 있는 값이 있어야 합니다. 

정렬 알고리즘들 선택할 때에는 효율성 외에도 중요한 특성들이 있습니다. 먼저 **안정성(stability)**은 입력 데이터 key값을 갖는 레코드가 여러개 있을 때, 정렬 후에도 이들의 상대적인 위치가 바뀌지 않는 것을 말합니다.


**제자리 정렬(in-place sorting)**은 입력 배열 이외에 추가적인 배열을 사용하지 않는 정렬을 말합니다. 효율성이 같다면 안정성을 갖고 제자리 정렬 특성이 있는 알고리즘이 더 우월합니다.

## 선택 정렬

**선택 정렬(selection sort)**은 리스트에서 가장 작은 숫자를 하나씩 찾아 순서대로 저장하는 것입니다.


위에 알고리즘은 단순하지만 한가지 문제가 있습니다. 정렬을 위해 입력 리스트 외에 추가적인 리스트가 필요한 것입니다. 최솟값이 선택되면 이 값을 출력 리스트에 저장하는 것이 아니라 입력 리스트의 첫 번째 요소와 교환하는 것으로 **제자리 정렬**로 개선할 수 있습니다.


```python
def selection_sort(A):
	n = len(A)
	for i in range(n-1):
		least = i
		for j in range(i+1, n):
			if(A[j] < A[least]):
				least = j
		# 파이썬에서 사용되는 두 변수 교환 방식
		A[i] , A[least] = A[least], A[i]
```


### 선택 정렬의 특징

- 알고리즘은 간단하지만, 시간 복잡도 ○(n²)으로 효율적이지 않습니다.
- 안정성을 만족하지도 않습니다.
- 제자리 정렬로 추가적인 리스트가 필요하지 않습니다.
- 자료의 구성에 상관없이 연산의 횟수가 결정된다는 장점이 있습니다. 이것은 정렬할 리스트의 크기가 정해지면 리스트에 어떤 숫자가 어떻게 들어가 있는지와 무관하게 정렬에 걸릴 시간을 예측할 수 잇는 것입니다.
- 리스트가 크기 않는 문제라면 충분히 사용할 수 있는 알고리즘입니다.

## 삽입 정렬

삽입 정렬은 정렬된 부분 리스트에 요소를 끼워 넣어 정렬하는 것을 말합니다.

```python
def insertion_sort(A):
	n = len(A)
	for i in range(1, n):
		key = A[i]
		j = i-1
		while j >= 0 and A[j] > key:
			A[j + 1] = A[j]
			j -= 1
		A[j + 1] = key
```

### 삽입 정렬의 특징

- 입력의 구성에 따라 처리시간이 달라지는데, 최악의 상황에 대한 시간 복잡도가 ○(n²)으로 효율적이지 않은 알고리즘입니다.
- 끼워 넣기를 위해 많은 레코드의 이동이 필요하므로 레코드의 크기가 큰 경우 선택 정렬보다도 효율적이지 않습니다.
- 제자리 정렬이고, 안정성도 충족합니다.(왜 안정성을 충족?)
- 레코드 대부분이 이미 정렬된 경우라면 효율적으로 사용될 수 있습니다.

## 퀵 정렬

기준을 두고 분할하여 정렬하는 방법을 말합니다.


```python
def quick_sort(A, left, right):
	if left < right:
		q = partition(A, left, right)
		quick_sort(A, left, q - 1)
		quick_sort(A, q + 1, right)
```

### 분할은 어떻게 할까?

분할의 아이디어는 탐색-교환 과정을 반복하는 것입니다.

탐색은 low를 오른쪽으로 high를 왼쪽으로 진행하면서 조건에 맞지 않는 요소를 찾는 과정입니다.

- 왼쪽 부분 리스트: A[low]가 피벗 이하이면 왼쪽 부분 리스트에 적합하므로 low를 오른쪽으로 전진시키다가, A[low]가 피벗보다 클 때 멈춥니다.
- 오른쪽 부분 리스트: A[high]가 피벗보다 크면 high를 왼쪽으로 전진시키다가 [high]가 피벗보다 작으면 멈춥니다.
1. 1번째 그림은 low와 high 모두 첫 번째 위치에서 조건이 맞지 않아 탐색이 중지합니다. 이제 양쪽에서 조건이 맞지 않는 A[low]와 A[high]를 찾았으니 이들을 교환



1. 다시 탐색을 진행하여, low는 164, 167, 170, 162를 지나 176에서 멈춥니다. high는 182를 지나 159에서 멈춥니다.
    
    
    다시 조건이 맞지 않는 A[low]와 A[high]를 찾았으니 이들을 교환합니다.
    
2. 다시 탐색을 진행합니다. low는 176에서 멈추고 high는 159에서 멈춥니다.
    
    
    그런데 이제 low가 high보다 더 큰 상황이 되었습니다. low와 high가 역적되면 탐색-교환 과정은 종료됩니다.
    
3. 피벗과 high의 항목을 교환하면 됩니다.
    
    

```python
def partition(A, left, right):
	pivot = A[left]
	low = left + 1
	high = right
	
	while(low < high):
		while low <= right and A[low] <= pivot:
			low += 1
		
		while high >= left and A[high] > pivot:
			high -= 1
		
		if low < high :
			A[low], A[high] = A[high], A[low]
	
	A[left], A[high] = A[high], A[left]
	return high
```

### 퀵 정렬의 특징

- 최악의 경우는 좋지 않지만, 평균적인 경우는 최선의 경우에 비해 추가적인 연산이 39% 정도만 늘어나는 것으로 알려져 있습니다. 결국 평균적으로 최선의 입력과 비슷한 속도가 나옵니다.
- 불필요한 데이터의 이동을 줄이고 먼 거리의 데이터를 교환하며, 한번 결정된 피벗들이 추후 연산에서 제외되어 병합 정렬이나 힙 정렬에 비해 매우 빠른 알고리즘

## 기수 정렬

키값을 비교하지 않고도 효율적인 비교 기반 정렬들보다 이론적으로 더 빨리 정렬할 수 있습니다. 기수란 숫자의 자릿수를 말합니다. 예를 들면 숫자 42는 4와 2의 두개의 자릿수를 가지고 이것이 기수가 됩니다.

기수 정렬은 여러개의 버킷을 사용하는데, 이것은 큐 구조 입니다.

### 한 자리 자연 수의 정렬


### 여러 자리 자연수의 정렬

[28, 93, 39, 81, 62, 72, 38, 26] 기수 정렬을 해보겠습니다. 기수 정렬 방법은 두가지가 있습니다. 효과적인 방법을 사용하여 정렬을 진행하겠습니다.

- 간단한 방법의 기수 정렬: 0~99번까지 번호가 매겨진 100개의 버킷을 사용
- 효과적인 방법의 기수 정렬: 1의 자리와 10의 자리를 따로따로 정렬



### 기수 정렬 알고르즘

```python
from collections import deque

BUCKETS = 10 
DIGITS = 2 # 최대 2자릿수 숫자를 정렬
def radix_sort(A):
	queues = []
	for i in range(BUCKETS):
		queues.append(deque())
	
	n = len(A)
	factor = 1
	for d in rande(DIGITS):
		for i in range(n):
			queues((A[i]//factor) % BUCKETS).append(A[i])
		
		i = 0
		for b in range(BUCKETS):
			while queues[b]:
				A[i] = queue[b].popleft()
				i += 1
		factor *= BUCKETS
		print("step", d+1, A)
```

### 기수 정렬의 특징

- 만약 리스트의 요소가 실수이거나 한글, 한자라면 적용이 어렵습니다. 즉, 제한된 응용에만 사용할 수 있는 알고리즘
- 버킷을 위한 추가적인 메모리가 필요

## 파이썬 정렬함수

```python
# 리스트의 sort 메소드
data = [6,3,7,4,9,1,5,2,8]
data.sort()
data.sort(reverse=True)

# 파이썬의 내장 함수
data2 = [6,3,7,4,9,1,5,2,8]
result = sorted(data2)
result2 = sorted(data2, reverse=True)

# 복잡한 레코드 정렬
data3 = [(62, 88, 81), (50, 3, 31), (86, 53, 42), (73, 47, 4), (89, 9, 8),
(47, 88, 55), (19, 18, 20), (15, 1, 88), (90, 6, 60), (41, 92, 19)]

def keyfunc(p):
	return p[0]

x_inc = sorted(data3, key = keyfunc)

# 람다 함수
x_inc = sorted(data3, key = lambda p : p[0]) # x정렬
y_dec = sorted(data3, key = lambda p : p[1], reverse=True) # y 정렬
```

