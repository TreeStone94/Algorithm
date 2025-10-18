## 큐란?

큐는 가장 먼저 들어간 자료가 가정 먼저 나오는 자료구조입니다. 큐는 매표소의 대기줄을 떠올리면 쉽게 이해할 수 있습니다. 매표소에서는 먼저 온 사람이 먼저 표를 사게 되고, 방금 도착한 사람은 줄을 서 있는 사람들의 맨뒤에서 자신의 순서를 기다려야 합니다.

큐는 이처럼 먼저 들어온 데이터가 먼저 나가는 **선입선출(FIFO: First-in First-Out)**의 특성을 갖는 자료구조입니다. 큐는 스택과 비슷해 보이지만 삽입과 삭제 연산이 같은 쪽이 아니라 서로 다른 쪽에서 일어난다는 근복적인 차이가 있습니다. 즉, A, B, C를 순서대로 넣으면(삽입) 꺼낼(삭제) 때도 같은 순서인 A, B, C로 나오게 됩니다. 이때 삽입이 일어나는 곳을 **후단(rear)**이라고 하고 삭제가 일어나는 곳을 **전단(front)**이라 부릅니다.


일상생활에서 많은 일들이 발생한 순서대로 처리되어야 하는 것처럼 컴퓨터에서도 큐가 필요한 곳은 매우 광범위합니다. 예를 들어, 컴퓨터와 주변 기기 사이에는 항상 큐가 있는데, 컴퓨터의 빠른 CPU와 속도가 상대적으로 느린 주변장치(예: 프린터)들 **사이의 시간이나 속도 차이를 극복하기 위한 임시 기억장치(Buffer)**로 사용됩니다. 또한, 컴퓨터로 현실 세계를 시뮬레이션하는 분야에서도 큐가 폭넓게 사용됩니다. 이러한 큐는 다양한 알고리즘에서도 흔히 사용되는 매우 중요한 도구입니다.

### 큐의 연산

스택과 마찬가지로 큐에도 숫자나 문자열을 포함한 어떤 자료든 저장할 수 있습니다. 연산도 스택과 유사합니다. 큐에서도 역시 삽입과 삭제가 가장 핵심적인 연산이고, 큐의 상태를 살피는 연산들을 다암과 같이 추가할 수 있습니다.

<aside>
💡 큐의 연산

- enqueue(e): 새로운 요소 e를 큐의 맨뒤에 추가
- dequeue(): 큐의 맨 앞에 있는 요소를 꺼내서 반환
- isEmpty(): 큐가 비어 있으면 True, 아니면 False 반환
- peek(): 큐의 맨 앞에 있는 요소를 삭제하지 않고 반환
- size(): 큐에 들어 있는 전체 요소의 수를 반환
</aside>


큐에서도 두 가지 오류 상황을 만날 수 있는데, 포화 상태인 큐에 `enqueue()` 연산을 실행하는 경우 오버플로 오류와 공백인 큐에서 `dequeue()` 나 `peek()` 연산을 실행하는 경우 발생하는 언더플로 오류입니다.

## 배열로 구현하는 큐

큐도 배열 구조와 연결된 구조로 구현할 수 있습니다.

### 배열 구조의 큐를 위한 데이터


- array[]: 큐 요소들을 저장하는 배열
- capacity: 큐에 저장할 수 있는 요소의 최대 개수
- rear: 맨 마지막(후단) 요소의 위치(인덱스)
- front: 첫 번째(전단) 요소 바로 이전의 위치(인덱스)
### 선형 큐의 문제점과 원형 큐의 원리

용량이 5인 공백 상태의 큐에 요소 A~E를 삽입(enqueue)하고 두번의 삭제(dequeue)를 순서대로 수행했다고 생각해 봅시다.  이 상태에서 F를 삽입(enqueue(F))하려면 문제가 생깁니다. 큐의 앞부분에 공간이 있는데도 rear를 더 증가 시킬 수 없으므로 새로운 요소 F를 후단에 삽입할 수 없는 것입니다.


그렇다면 어떻게 해야 할까요? 어쩔 수 없이 큐의 요소들을 모두 최대한 앞으로 옮겨 후단에 공간을 확보한 다음 삽입해야 합니다. 이렇게 동작하는 큐를 **선형 큐(linear queue)**라고 하는데, 동작을 이해하기는 쉽지만 요소들의 이동이 필요하므로 효율적이지 않습니다.

이러한 선형큐의 문제를 깔끔하게 해결할 수 있는 아이디어가 있습니다. 배열을 선형이 아니라 원형으로 생각하는 것입니다. 이러한 큐를 **원형 큐(circular queue)**라고 하는데, 실제로 배열이 원형이 되는 것이 아니라 인덱스 **front와 rear를 원형으로 회전시키는 개념**입니다. `enqueue(F)` 가 호출되면 오른쪽과 같이 rear를 시계 방향으로 한칸 회전시키고 그 위치에 F를 저장하는 것입니다.


시계 방향의 회전은 어떻게 할까요? front나 rear가 계속 증가하다가 용량(capacity)과 같아지면 이들을 다시 0으로 만들어주면 됩니다. 이것은 If와 같은 조건문으로 처리할 수도 있지만, 다음과 같이 나머지 연산(%)을 이용하면 더 간격하게 처리 됩니다.

- 전단 회전: front ← (front+1) % capacity
- 후단 회전: rear ← (rear+1) % capacity

예를 들어, 삽입과 관련된 rear는 0, 1, 2, 3, 4의 순으로 증가하다가 (4+1)%5가 되어 다시 0으로 되돌아갑니다. 삭제와 관련된 front도 같은 방법으로 시계 방향으로 회전 합니다. 

### 원형 큐의 클래스 구현

- **클래스 선언과 멤버변수 초기화**

```python
class ArrayQueue :
	def __init__( self, capacity = 10) :
		self.capacity = capacity
		self.array = [None] * capacity
		self.front = 0
		self.rear = 0
```

- **공백 상태와 포화 상태를 검사하는 isEmpty()와 isFull() 연산**

공백 상태는 front == rear인 경우입니다. 이들이 0이 되어야 할 필요는 없습니다. 단지 front와 rear가 같은 곳을 가리키기만 하면 큐는 공백 상태 입니다.


오류 상태는 front == rear인 상태로 공백 상태와 구분이 되지 않습니다. 따라서 원형 큐에서는 보통 하나의 자리를 비워두는 전략을 사용합니다. 즉, (b)와 같이 **front가 near의 바로 다음에 있으면 포화 상태**라고 정의합니다. 시계 방향의 회전까지 고려하면 front == (rear+1)% capacity가 포화 상태 입니다.

```python
	def isEmpty(self):
		return self.front == self.rear
	
	def isFull(self):
		return self.front == (self.rear+1)%self.capacity
```

- **새로운 요소 e를 삽입하는 enqueue(e) 연산**

후단 rear를 먼저 시계 방향으로 한칸 회전시키고, 그 위치에 새로운 요소 e를 복사하면 됩니다. 물론 삽입은 포화 상태가 아니어야 가능합니다.

```python
	def enqueue( self, item ):
		if not self.isFull():
			self.rear = (self.rear + 1) % self.capacity
			self.array[self.rear] = item
		else : pass
```

- **맨 앞의 요소를 삭제하는 dequeue() 연산**

삭제는 큐에 요소가 남아 있어야 가능합니다. 큐가 공백이 아니면 먼저 front를 시계 방향으로 한칸 회전시키고 그 위치의 요소를 반환하면 됩니다.

```python
	def dequeue( self ):
		is not self.isEmpty():
			self.front = (self.front + 1) % self.capacity
			return self.array[self.ront]
		else: pass
```

- **맨 앞의 요소를 들여다보는 peek() 연산**

front를 시계 방향으로 한칸 회전 시킨 위치를 요소를 반환하면 됩니다.

```python
	def peek(self):
		if not self.isEmpty():
			return self.array[(self.front + 1)%self.capacity]
		else: pass
```

- **전체 요소의 수를 구하는 size() 연산**

만약 rear-front가 음수라면 추가로 용량을 더해 양수로 만들어야 합니다. 따라서 원형 큐의 전체 요소의 수는 (rear-front+capacity)%capacity가 됩니다. 그림과 같이 전체 요소의 수는 (0-2+5)%5=3 입니다.


```python
	def size( self ):
		return (self.rear - self.front + self.capacity) % self.capacity
```

- **큐의 내용을 출력하는 display() 연산**

원형 큐에 저장된 모든 요소를 큐에 들어온 순서대로 출력하는 연산을 구현해 보겠습니다. 맨 앞 요소는 그림과 같이 front의 다음 위치(front+1)에 있으며, 출력할 요소의 수는 size()개 입니다. 물론 인덱스는 시계 방향으로 회전되어야 하므로 나머지 연산을 적용해야 합니다.


```python
	def display(self, msg):
		print(msg, end='= [')
		for i in range(self.front+1, self.front+1+self.size()):
			print(self.array[i%self.capacity], end= ' ')
		print(']')
```

### 큐의 활용

원형 큐의 동작을 확인하기 위해 간단한 프로그램을 만들어 보겠습니다. 무작위로 발생한 정수(0~99)를 큐가 꽉 찰 때 까지 삽입한 후, 다시 모든 숫자를 꺼내 출력하는 것 입니다.

```python
import random
	q = ArrayQueue(8)
	
	q.display("초기 상태")
	while not q.isFull():
		q.enqueue(random.randint(0,100))
	
	q.display("포화 상태")
	
	print("삭제 순서: ", end='')
	while not q.isEmpty():
		print(q.dequeue(), end=' ')
	print()
```

### 원형 큐를 링 버퍼로 사용하기

원형 큐는 오래된 자료를 버리고 항상 최근의 자료를 유지하는 용도로 사용할 수 있습니다. 예를 들어, 그림과 같이 최대 7개의 요소를 저장할 수 있는 원형 큐에 7개 이상의 자료들이 연속적으로 입력되었을 때 **가장 최근에 들어온 7개만 저장되도록 하고 오래된 데이터는 버리는 것**입니다. 이러한 원형 큐를 **링 버퍼(ring buffer)**라고 합니다.


포화 상태에서 삽입연산을 추가로 수행하면 기존의 원형 큐에서는 오버플로 오류가 발생하고 삽입은 실패합니다. 이에 비해 링 버퍼에서는 원형 큐의 enqueue를 약간 수정하여 포화 상태와 상관없이 항상 삽입할 수 있도록 합니다. 물론 이 과정에서 가장 오래된 요소가 버려집니다. (c)와 같이 포화 상태가 되더라도 무조건 다음 위치에 데이터(7)를 일단 삽입합니다. 삽입이 끝나면 front와 rear가 같아지는 오류 상태가 되는데, 이때 front를 하나 증가 시킵니다. 즉, **가장 오래된 데이터를 삭제해서 큐를 계속 포화 상태로 유지**하는 것 입니다.

```python
	def enqueue2( self, item ):
		self.rear = (self.rear + 1) % self.capacity
		self.array[self.rear] = item
		if self.isEmpty():
			self.front = (self.front + 1) % self.capacity

q = ArrayQueue(8)

q.display("초기 상태")
for i in range(6):
	q.enqueue2(i)
q.display("삽입 0-5")

q.enqueue2(6)
q.enqueue2(7)
q.display("삽입 6,7")

q.enqueue2(8)
q.enqueue2(9)
q.display("삽입 8,9")

q.dequeue()
q.dequeue()
q.display("삭제 x2")
```


배열과 용량은 스택에서와 동일합니다. 스택에서 상단(top)만 사용한 것에 비해 큐는 두개의 변수가 필요한데, 삽입과 삭제가 다른 쪽에서 이루어져야하기 때문입니다. 먼저 후단을 나타내는 rear는 큐의 마지막 요소를 가리키면 됩니다. front는 큐의 첫번째 요소가 아니라 그 요소 바로 앞의 위치를 가리키도록 하겠습니다.

## 덱이란?

덱(deque)은 **double-ended queue**의 줄임말로서 전단과 후단에서 모두 삽입과 삭제가 가능한 큐를 말합니다. 그렇지만 여전히 중간에 삽입하거나 삭제하는 것은 허용하지 않습니다.


<aside>
💡 덱의 연산

- addFront(e): 새로운 요소 e를 전단에 추가
- addRear(e): 새로운 요소 e를 후단에 추가
- deleteFront(): 덱의 전단 요소를 꺼내서 반환
- deleteRear(): 덱의 후단 요소를 꺼내서 반환
- getFront(): 덱의 전단 요소를 삭제하지 않고 반환
- getRear(): 덱의 후단 요소를 삭제하지 않고 반환
- isEmpty(): 덱이 비어있으면 True를 아니면 False
- isFull(): 덱이 가득 차 있으면 True를 아니면 False
- size(): 덱에 들어 있는 전체 요소의 수를 반환
</aside>

덱은 스택과 큐의 연산을 모두 가지고 있습니다.

- 덱의 `addRear` , `deleteFront` , `getFront` 연산은 각각 큐의 `enqueue` , `dequeue` , `peek` 연산과 동일합니다.
- 덱의 후단(rear)을 스택 상단(top)으로 사용한다면, 덱의 `addRear` , `deleteRear` , `getRear` 연산은 스택의 `push` , `pop` , `peek` 연산과 동일합니다.

덱의 구현도 원형 큐와 비슷하게 원형 덱(circular deque)으로 구현하는 것이 좋습니다. 이때 주의해야 할 연산은 front와 rear를 감소시켜야 하는 deleteRear와 addFront입니다. 이들은 원형 큐의 enqueue나 dequeue 연산과는 달리 인덱스를 하나씩 줄여야하는데, 이것은 **반시계 방향 회전**을 의미 합니다. 이를 위한 인덱스 처리는 나머지 연산을 이용해 간결하게 할 수 있습니다.

- 전단 회전(반시계 방향): front ← (front -1 + capacity) % capacity
- 후단 회전(반시계 방향): rear ← (rear -1 + capacity) % capacity


후단 삭제를 위한 `deleteRear()` 를 수행하면 (b)와 같이 rear는 3에서 2로 줄어듭니다. 또한, (b)에서 전단 삽입을 위해 `addFront(D)` 를 수행하면 (c)와 같이 front는 0에서 7(=(0-1+8)%8)로 회전합니다.

## 상속을 이용한 덱의 구현

원형 덱은 어떻게 구현할 수 있을까요? 먼저 떠오르는 방법은 원형 큐와 같이 클래스를 만들고 각 연산을 하나씩 구현해 넣는 것입니다. 그런데 좀 더 편리한 방법이 있습니다. **상속(inheritance)**이라는 객체지향 프로그래밍 기법을 사용하는 것입니다. 


`isEmpty`, `isFull`, `size` 연산은 이름과 동작이 모두 같고, `deleteFront` , `getFront` , `addRear` 는 큐에 있는 연산인데 이름만 바뀐 것입니다. 새로 추가되는 연산은 `addFront`, `getRear`, `deleteRear` 뿐입니다.

상속은 매우 짧은 코드로 기존의 복잡한 클래스에 기능을 추가한 새로운 클래스를 만들 수 있는 매우 유용한 방법 입니다. 원형 큐를 상속해서 원형 덱을 구현하면 다음과 같은 장점들이 있습니다.

- 데이터는 추가로 정의할 필요없음
- `isEmpty`, `isFull` 도 추가로 정의할 필요 없음
- `deleteFront` , `getFront` , `addRear` 는 구현해야 하지만 단순히 원형 큐의 `enqueue` , `dequeue` , `peek` 연산을 호출하면 됨
- `addFront`, `getRear`, `deleteRear`  새로 구현

### 원형 큐를 상속하여 구현하는 원형 덱 클래스

- **클래스의 상속과 멤버변수 초기화**

앞에서 구현한 원형 큐 클래스 ArrayQueue를 상속하여 새로운 원형 덱 클래스 CircularDeque를 만들어 보겠습니다.

```python
class CircularDeque(AraayQueue):
	def __init__( self, capacity=10):
		super().__init__(capacity)
```

생성자에서 front, rear, array와 같은 변수를 선언하지 않았지만 이들은 부모 클래스의 데이터 멤버이므로 이미 자식 클래스에 들어있습니다. 따라서 자식 클래스에서 self.front와 같이 바로 사용하면 됩니다.

- **addRear(e), deleteFront(), getFront() 연산**

이 연산들은 원형 큐에 이미있지만 이름이 다릅니다. 따라서 이들은 자식 클래스에 멤버함수로 추가하고, 이미 구현된 부모 클래스의 해당 연산을 호출하면 됩니다.

```python
	def addRear( self, item ): self.enqueue(item)
	def deleteFront(self): return self.dequeue()
	def getFront(self): return self.peek()
```

- **addFront(e), deleteRear(), getRear() 연산**

```python
	def addFront( self, item ):
		is not self.isFull():
			self.array[self.front] = item
			self.front = (self.front -1 + self.capacity) % self.capacity
		else: pass
	
	def deleteRear(self):
		is not self.isEmpty():
			item = self.array[self.rear]
			self.rear = (self.rear - 1 + self.capacity) % self.capacity
			return item
		else: pass
		
	def getRear(self):
		is not self.isEmpty():
			return self.array[self.rear]
		else: pass
```

### 원형 덱의 활용

```python
dq = CirularDeque()

for i in range(9):
	if i%2==0: dq.addRear(i)
	else: dq.addFront(i)

dq.display("홀수는 전단 짝수는 후단 삽입")

for i in range(2): dq.deleteFront()
for i in range(3): dq.deleteRear()
dq.display("전단 삭제 2번, 후단 삭제 3번")

for i in range(9,14): dq.addFront(i)
dq.display("전단에 9 ~ 13 삽입")
```


## 파이썬에서 큐와 덱 사용하기

파이썬 리스트는 스택으로 사용하기는 충분하지만, 원형 큐나 덱으로 직접 사용하기에는 적절하지 않습니다. 따라서 파이썬에서 제공하는 모듈을 사용하는 것이 좋습니다.

### queue 모듈의 Queue 사용하기

파이썬 queue 모듈은 스택과 함께 큐를 제공해 주는데, 큐 클래스 이름은 Queue입니다. 

```python
import queue
q = queue.Queue(maxsize-20)
```

maxsize는 큐의 용량인데, 만약 maxsize가 0이면 용령의 제한이 없는(무한대의) 큐 객체를 만든다는 의미입니다.


```python
import queue
import random

q = queue.Queue(8)

print("삽입 순서: ", end='')
while not q.full():
	v = random.randint(0,100)
	q.put(v)
	print(v, end=' ')
print()

print('삭제 순서: ', end='')
while not q.empty():
	print(q.get(), end=' ')
print()
	
```

### collections모듈의 deque 클래스 사용하기

파이썬은 `collections` 라는 모듈에서 내장 자료형인 튜플이나 딕셔너리에 대한 확장 데이터 구조들을 제공하는데, `defaultdict` , `counter` , `deque` , `namedtuple` 등 다양한 클래스를 포함하고 있습니다.

```python
import collections
dq = collections.deque()
```


```python
import collections
dq = collections.deque()

print("덱은 공백 상태 아님" if dq else "덱은 공백 상태")
for i in range(9):
	if i%2 == 0: dq.append(i)
	else: dq.appendleft(i)
print("홀수는 전단 짝수는 후단 삽입", dq)

for i in range(2): dq.popleft()
for i in range(3): dq.pop()
print("전단 삭제 2번, 후단 삭제 3번",  dq)

for i in range(9,14): dq.appendleft(i)
print("전단에 9 ~ 13 삽입        ", dq)

print("덱은 공백 상태 아님" if dq else "덱은 공백 상태")
```


삽입 연산은 rear를 먼저 하나 증가시킨 후 그 자리에 새로운 요소를 넣으면 됩니다. 삭제 연산은 front를 하나 증가시킨 후 그 자리의 요소를 반환하면 됩니다. 맨 처음에는 큐가 공백이어야 하므로 front와 rear를 모두 -1로 초기화 합니다.
