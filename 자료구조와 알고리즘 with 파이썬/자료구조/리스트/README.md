## 리스트란?

리스트 또는 선형 리스트(linear list)는 자료들이 차례대로 나열된 선형 구조입니다. 이때 각 자료는 순서 또는 위치를 가집니다.


리스트에서는 어떤 위치에서도 새로운 요소를 삽입할 수 있습니다. 이때 중요한 것은 어느 위치에 요소를 삽입하려면 이후 모든 자료가 한 칸씩 뒤로 밀린다는 것입니다. 삭제도 마찬가지입니다. 어느 위치의 요소를 삭제하면 이후의 모든 요소의 위치가 변경됩니다. 공백 상태의 리스트에 A와 B가 삽입된 상태 (c)에서 위치 1에 C를 삽입하면 B가 한 칸 뒤로 밀립니다. 다음으로 위치 0인 요소를 삭제하면 (e)와 같이 A가 나오고 이후 C와 B가 앞으로 한 칸씩 당겨집니다.


스택이나 큐, 덱에서도 자료들을 일렬로 저장하지만 자료의 대한 접근은 전단이나 후단으로 제한되었습니다. 그러나 리스트는 이러한 제한이 없습니다. 따라서 가장 활용이 자유로운 선형자료구조입니다. 물론 자유로운 만큼 고려해야 할 사항들도 많고, 코드도 복잡해질 것입니다.

리스트는 **집합(set)**과 유사한 점이 많지만 중요한 차이가 있습니다. 리스트에서는 순서가 있지만 **집합은 원소 사이에 순서가 없습니다.** 또한, **집한은 원소의 중복을 허용하지 않습니다.** 특히 집한은 원소 사이에 순서의 개념이 없으므로 선형 자료구조라 볼수 없습니다.

### 리스트의 연산

<aside>
💡리스트의 연산
- insert(pos, e): pos 위치에 새로운 요소 e를 삽입
- delete(pos): pos 위치에 있는 요소를 꺼내서 반환
- getEntry(pos): pos 위치에 있는 요소를 삭제하지 않고 반환
- isEmpty(): 리스트가 비어 있으면 true, 아니면 false
- isFull(): 리스트가 가득차있으면 true, 아니면 false
- size(): 리스트에 들어 있는 전체 요소의 수 반환
</aside>

## 배열 구조와 연결된 구조

리스트도 배열 구조와 연결된 구조로 구현할 수 있습니다.

**모든 요소는 중간에 빈자리가 없이 반드시 메모리의 연속된 공간에 저장**되어야 합니다. 요소들이 연속된 공간에 있으면 원하는 위치의 요소를  빠르게 참조하고 관리할 수 있습니다.


이에 비해, 연결된 구조에서는 요소들을 메모리의 한군데 모아두는 것을 포기합니다. 즉, 요소들이 메모리의 여기저기에 흩어져서 저장되는 것입니다. 그렇다면 흩어진 요소들은 어떻게 순서대로 관리할 수 있을까요? **링크(link)**를 이용하면  됩니다. 즉, 요소들이 다른 요소를 가리키는 하나 이상의 링크를 갖도록 하여 전체를 순서대로 연결해 관리하는 것입니다.

이처럼 메모리에 흩어져 있는 요소들을 링크로 연결해 하나로 관리하는 것을 **연결된 구조(linked structure)**라고 합니다. 특히 자료들을 링크를 통해 일렬로 나열할 수 있는 연결된 구조를 **연결 리스트(linked list)**라고 부릅니다. 연결된 구조에서 하나의 상자를 노드(node)라고 부르는데, 데이터와 함께 링크를 갖습니다. 배열 구조와는 달리 하나의 요소를 표현하기 위해 링크가 추가로 필요한 것에 유의하세요. 연결된 구조에서는 이러한 링크의 수를 여러 개로 늘리면 리스트와 같은 선형 자료 구조뿐만 아니라 트리나 그래프와 같이 훨씬 복잡한 구조들도 효율적으로 표현 할 수 있습니다.
## 배열 구조와 연결된 구조

리스트도 배열 구조와 연결된 구조로 구현할 수 있습니다.

**모든 요소는 중간에 빈자리가 없이 반드시 메모리의 연속된 공간에 저장**되어야 합니다. 요소들이 연속된 공간에 있으면 원하는 위치의 요소를  빠르게 참조하고 관리할 수 있습니다.


이에 비해, 연결된 구조에서는 요소들을 메모리의 한군데 모아두는 것을 포기합니다. 즉, 요소들이 메모리의 여기저기에 흩어져서 저장되는 것입니다. 그렇다면 흩어진 요소들은 어떻게 순서대로 관리할 수 있을까요? **링크(link)**를 이용하면  됩니다. 즉, 요소들이 다른 요소를 가리키는 하나 이상의 링크를 갖도록 하여 전체를 순서대로 연결해 관리하는 것입니다.

이처럼 메모리에 흩어져 있는 요소들을 링크로 연결해 하나로 관리하는 것을 **연결된 구조(linked structure)**라고 합니다. 특히 자료들을 링크를 통해 일렬로 나열할 수 있는 연결된 구조를 **연결 리스트(linked list)**라고 부릅니다. 연결된 구조에서 하나의 상자를 노드(node)라고 부르는데, 데이터와 함께 링크를 갖습니다. 배열 구조와는 달리 하나의 요소를 표현하기 위해 링크가 추가로 필요한 것에 유의하세요. 연결된 구조에서는 이러한 링크의 수를 여러 개로 늘리면 리스트와 같은 선형 자료 구조뿐만 아니라 트리나 그래프와 같이 훨씬 복잡한 구조들도 효율적으로 표현 할 수 있습니다.

### 배열 구조의 리스트와 연결 리스트의 비교

1. **리스트 요소들에 대한 접근**


그림과 같이 리스트에서 원하는 요소에 접근하는 연산은 배열 구조가 훨씬 유리합니다. 그렇다면 연결된 구조를 왜 사용할까요? 당연히 그만한 장점이 있기 때문입니다.

1. **리스트의 용량**

기본적으로 배열은 용량이 고정됩니다. 고정된 용량은 중간에 부족하다고 늘리거나 필요 없다고 줄이기 어렵습니다. 리스트를 위해 배열을 사용할 때, 만약 배열을 무턱대고 너무 크게 할당해 놓으면 메모리 낭비가 심할 것입니다. 그렇다고 너무 적게 할당하면 빨리 포화 상태가 되어 새로운 요소를 넣지 못하는 상황이 발생합니다.


연결된 구조는 용량이 고정되어 있지 않습니다. 필요할 때 필요한 크키만큼 새로 할당해서 사용하는 것입니다. 따라서 메모리를 효율적으로 사용할 수 있습니다. 또한, 컴퓨터에 메모리가 남아 있는 한 계속 자료를 넣을 수 있습니다. 포화 상태가 될 수 없습니다.


1. **리스트의 삽입 연산**

배열 구조에서는 중간에 자료를 삽입하려면 그 위치 이후 모든 요소를 한 칸씩 뒤로 밀어야 합니다. 이처럼 배열 구조의 삽입은 많은 요소의 이동이 필요합니다. 


연결된 구조에서는 삽입할 위치를 알고 있다면 효율적인 삽입이 가능합니다. 그림과 같이 97의 링크와 새로운 요소 61의 링크만 수정하면 됩니다. 그 외의 다른 노드들은 전혀 영향을 받지 않는다는 것에 유의하세요. 결국, 연결된 구조의 삽입이 훨씬 효율적입니다.

1. **리스트의 삭제 연산**

삭제 연산도 마찬가지입니다. 배열 구조에서는 중간에 있는 자료를 삭제하면 이후의 모든 자료를 앞으로 당겨 빈 곳이 생기지 않도록 해야합니다. 만약 삭제할 요소가 앞쪽이라면 리스트의 요소 대부분을 이용해야 하므로 매우 비효율적입니다. 


이에 비해, 연결된 구조에서는 삭제할 노드 바로 앞 노드의 링크만 수정하면 되고, 다른 노드들은  수정할 필요가 없습니다. 결국, 연결된 구조의 삭제가 훨씬 효율적입니다.

| 배열 구조 | 연결된 구조 | 기능 | 효율성 |
| --- | --- | --- | --- |
| 연속된 구조 | 연결 구조 | 접근 | 배열 구조 |
| 용량 고정 | 용량 고정 X | 용량 | 연결된 구조 |
| 요소들의 많은 수정 필요 | 요소들의 적은 수정 | 삽입/삭제 | 연결된 구조 |
## 배열 구조의 리스트

파이썬의 리스트는 클래스로 구현되어 있는데 다양한 연산들을 메서드로 지원합니다.


### 파이썬 리스트는 용량 제한 없음

파이썬 리스트는 배열 구조를 사용하지만 용량이 제한되지 않도록 내부적으로 구현되어 있습니다. 용량이 8인 리스트 8개의 요소가 삽입되면 이제 리스트에는 여유 공간이 없습니다. 이 상태에서 `append(I)` 연산을 시도하면 어떻게 될까요? 만약 용량이 제한된 리스트라면 이 연산을 성공적으로 처리하지 못합니다.

그렇지만 파이썬 리스트는 이러한 상황을 용량을 늘리는 방법으로 해결합니다.


그렇다면 `append()` 연산은 얼마나 효율적일까요? 리스트의 용량이 포화되기 전이라 매우 빨리 처리됩니다. 만약 리스트가 포화 상태라면 위에 그림과 같이 처리가 필요하므로 훨씬 많은 시간이 거립니다. 메모리를 할당하고, 기존의 요소를 모두 복사하는 작업이 추가되어야 하기 때문입니다. 결국  파이썬 리스트의 append()연산은 처리 시간이 항상 같지는 않습니다. 그렇지만 용량 확장해야 하는 경우가 가끔 발생하고, 대부분은 여유 공간이 있어 빠르게 처리됩니다. 특히, 용량 확장은 내부적으로 처리되므로 리스트를 사용하는 사용자는 신경을 쓰지 않아도 됩니다.

## 연결된 리스트의 구조와 종류

### 연결 리스트의 구조

1. **노드**

연결 리스트에서 하나의 노드는 하나의 데이터와 함께 하나 이상의 링크를 갖습니다. 이 때 데이터는 배열 구조에서의 요소를 말하는데, 리스트에 저장하고 싶은 자료에 해당합니다. 링크는 다른 노드를 가리키는(다른 노드의 주소를 저장하는) 변수입니다. 배열 구조에 비해 연결된 구조에서는 링크를 위한 추가 공간이 필요합니다. 그러나 대부분은 데이터가 훨씬 크므로 링크를 위한 공간은 무시할 수 있습니다.

1. **헤드 포인터**

연결 리스트는 시작 노드만 알면 링크로 매달려 있는 모든 노드에 순차적으로 접근할 수 있는데, 이 노드를 보통 **머리 노드(head node)**라고 부릅니다. 머리 노드의 주소를 저장하는 변수를 **헤드 포인터(head pointer)**라고 하는데, 연결 리스트의 가장 중요한 정보입니다. 마지막 노드를 보통 **꼬리 노드(tail node)**라고 부르는데, 꼬리 노드의 링크를 처리하는 방법에 따라 단순 연결과 원형 연결로 구분됩니다.


### 연결 리스트의 종류

1. **단순 연결 리스트(singly linked list)**

하나의 방향으로만 연결된 리스트를 말합니다. 노드는 하나의 링크를 갖는데, 다음 노드의 주소가 저장됩니다.

1. **원형 연결 리스트(cirucular linked list)**

꼬리 노드의 링크를 약간 다르게 사용하면 원형으로 연결된 구조를 만들 수있습니다. 이러한 원형 연결 구조에서는 어떤 노드에서 시작해도 다른 모든 노드를 찾아 갈 수 있습니다. 하지만 노드들을 순서대로 방문할 때 종료 조건 처리에 매우 조심해야 합니다.


1. **이중 연결 리스트(doubly linked list)**

하나의 노드가 이전 노드와 다음 노드의 링크를 모두 갖도록 설계되었습니다. 두개의 링크를 갖는데, 하나는 이전 노드를, 다른 하나는 다음 노드를 가리키도록 하는 것입니다.


이전 노드를 위한 링크가 있으면 어떤 노드에서 이전 노드를 바로 찾아갈 수 있다는 장점이 있습니다. 편리한 만큼 링크를 이중으로 정확히 유지해야 하므로 코드가 복잡해집니다.


## 단순 연결 구조로 리스트 구현

### 노드 클래스 구현

```python
class Node:
	def __init__(self, elem, link=None):
		self.data = elem
		self.link = link
		
		def append(self, node):
			if node is not None:
				node.link = self.link
				self.link = node
			
		def popNext(self):
			next = self.link
			if next is not None:
				self.link = next.link
			return next
```

### 연결 리스트 클래스

연결된 구조에서는 리스트 클래스의 데이터 멤버로 어떤 것이 필요할까요? 의외로 단순합니다. 머리노드를 가리킬 변수 하나만 있으면 되는데 이를 head라 하겟습니다.


리스트가 공백 상태인 경우와 노드가 추가된 예를 보여주고 있는데, 전체 리스트를 관리하기 위해서는 head만 잘 처리하면 된다는 것을 알 수 있습니다.


```python
class LinkedList:
	def __init__(self):
		self.head = None
	
	def isEmpty(self):
		return self.head == None
	
	def isFull(self):
		return False # 연결된 구조에서는 포화 상태 없음
	
	def getNode(self, pos):
		if pos < 0: return None
		ptr = self.head
		for i in range(pos):
			if ptr == None:
				return None
			ptr = ptr.link
		return ptr
	
	def getEntry(self,pos):
		node = self.getNode(pos)
		if node == None: return Node
		else: return node.data
		
	def insert(self,pos,e):
		node = Node(e, None)
		before = self.getNode(pos-1)
		if before == None:
			node.link = self.head # 원래 head가 가리키고 있는 node를 삽입한 node가 가리키도록 함
			self.head = node
		else: before.append(node)
	
	def delete(self,pos):
		before = self.getNode(pos-1)
		if before == None:
			before = self.head
			if self.head is not None:
				self.head = self.head.link
			return before
		else: return before.popNext()
	
	def replace(self, pos, elem) :
     node = self.getNode(pos)
     if node != None : node.data = elem
			
	def size(self):
		ptr = self.head
		count = 0
		while ptr is not None:
			ptr = ptr.link
			count +=1
		return count
		
	def display(self, msg='LinkedList:'):
		print(msg, end='')
		ptr = self.head
		while ptr is not None:
			print(ptr.data, end='->')
			ptr = ptr.link
		print('None')
```

## 이중 연결 구조로 리스트 구현

### 이중 연결 구조 노드 클래스

```python
class DNode:
	def __init__(self, elem, prev=None, next=None):
		self.data = elem
		self.next = next
		self.prev = prev
	def append(self,node):
		if node is not None:
			node.next = self.next
			node.prev = self
			if node.next is not None:
				node.next.prev = node
			self.next = node
	def popNext(self):
			node = self.next
			if node is not None:
				self.next = node.next
				if self.next is not None:
					self.next.prev = self
			return node
```

### 이중 연결 리스트 클래스

```python
class DblLinkedList:
	def __init__(self):
		self.head = None
	
	def display(self, msg='DblLinkedList:'):
		print(msg, end='')
		ptr = self.head
		while ptr is not None:
			print(ptr.data, end='<=>')
			ptr = ptr.next
		print('None')
	
	def insert(self, pos, e):
		node = DNode(e)
		before = self.getNode(pos-1)
		if before == None:
			node.next = self.head
			if node.next is not None:
				node.next.prev = node
			self.head = node
		else: before.append(node)
	
	def delete(self,pos):
		before = self.getNode(pos-1)
		if before == None:
			before = self.head
			if self.head is not None:
				self.head = self.head.next
			if self.head is not None:
				self.head.prev = None
			return before
		else: before.popNext()
```

