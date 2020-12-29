# 알면 좋은 함수 / 라이브러리

## 내장	함수

---

- 문자열 함수
    1. s1.startswith(s2)

        s1 문자열이 s2로 시작하는 지 Boolean 리턴

- set
- list
    - 정렬
        - sorted(listName), sorted(listName, reverse = True) → 내림차순 정렬 : 정렬된 리스트 리턴
        - listName.sort() : 리스트를 정렬시킴
    - 복사
        - list는 copy by reference 이므로 주의해야함
        - copy by value 하고 싶으면 list2 = list1[:]
        - for loop의 조건으로 리스트를 사용할 때 for loop 에서 list 값을 바꾸면 조건검사할때마다 변경된 리스트에 접근하게 됨. 주의주의 ⭐️
- tuple
- zip

    같은 개수의 자료형을 묶어주는 함수

    ```python
    Number = [1,2,3,4]
    Name = ['hong','gil','dong','nim']
    Number_Name = list(zip(Number,name))
    print(Number_Name)

    #결과 : [(1 ,'hong'), (2 ,'gil'), (3 ,'dong'), (4 ,'nim')]
    ```

    단, 

    1. **set과 같이 순서가 없는 자료형**은 순서대로 묶이지 않음!
    2. 개수가 다를 경우 더 적은 것에서 짤림.

- enumerate

    enumerate(list_name) 하면 [ (0, 'apple'), (1, 'banana') ] 이런식으로 순서쌍 생성.

    for문과 결합하여 많이 사용

    ```python
    for idx, val in enumerate(fruit):
    	print(idx,val)
    ```

- 클래스와 메서드

    ```python
    class Person:
    	def __init__(self,parameter1,parameter2,parameter3): #initializer
    		self.myAttribute1 = parameter1
    		self.myAttribute2 = parameter2
    		self.__privateAttribute = paramater3 # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
    		# 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함
    	def greeting(self):
    		print('Hello')
    ```

- list.sort() 와 sorted()

    list.**sort()** 메서드는 리스트에게만 정의되고. in-place 수정. None 반환.

    **sorted()** 함수는 모든 이터러블을 받아들인다. 새로운 정렬된 리스트를 만든다.

    key 매개 변수의 값은 단일 인자를 취하고 정렬 목적으로 사용할 키를 반환하는 함수여야 합니다. 키 함수가 각 입력 레코드에 대해 정확히 한 번 호출되기 때문에 이 기법은 빠릅니다. 딕셔너리에서 sorted 사용하면 key를 소트하여 key 리스트를 return한다. 

- 람다 lambda

    > lambda 인자 : 표현식

    > map(함수, 리스트)

    ```python
    (lambda x,y: x + y)(10, 20)
    # 30

    (lambda x: x*3)(10)
    # 30

    list(map(lambda x: x ** 2, range(5)))  
    # [0, 1, 4, 9, 16]
    ```

    ### sort의 key로 활용되는 lambda

    ```python
    target = [[1,2],[3,1],[2,6],[4,5],[3,3]]

    #2번째 인덱스로 비교를 하고 싶다면 x[0] 대신 x[1] 입력

    target.sort(key = lambda x:x[0])

    #1번째 인덱스로 정렬후 값이 같을 때 2번째 인덱스로 내림차순 정렬하고 싶다면 이렇게
    target.sort(key = lambda x:x[0],-x[1])
    ```

- divmod(a,b)

    a/b의 몫과 나머지를 순서대로 튜플 형태로 리턴

- 이차원리스트 → 일차원리스트

    ```python
    my_list = [[1, 2], [3, 4], [5, 6]]

    answer = []
    for i in my_list:
        answer += i

    # 방법 1 - sum 함수
    answer = sum(my_list, [])

    # 방법 2 - itertools.chain
    import itertools
    list(itertools.chain.from_iterable(my_list))

    # 방법 3 - itertools와 unpacking
    import itertools
    list(itertools.chain(*my_list))

    # 방법4 - list comprehension 이용
    [element for array in my_list for element in array]

    # 방법 5 - reduce 함수 이용1
    from functools import reduce
    list(reduce(lambda x, y: x+y, my_list))

    # 방법 6 - reduce 함수 이용2
    from functools import reduce
    import operator
    list(reduce(operator.add, my_list))

    # 방법 7 - numpy 라이브러리의 flatten 이용
    import numpy as np
    np.array(my_list).flatten().tolist()
    ```

- 아스키코드
- 바이너리
- 

## 라이브러리

---

- itertools
    - 순열 : itertools.permutations
    - 중복순열 : itertools.product(arr,arr) → 원래 product는 주어진 배열에서 하나씩 뽑아서

        ```python
        from itertools import product
        list1 = ['a','b','c','d','e']
        list2 = [1,2,3]
        product(list1,list2)
        #두 리스트의 곱집합
        product(list1,repeat=2)
        #리스트에서 중복해서 두개뽑은거 리턴
        ```

    - 조합 : itertools.combinations(iterable,r)
    - 중복조합 : itertools.combinations_with_replacement(iterable,r)
    - 함수 없이 구현 참고자료

    [안녕하세요? 딥러닝 머신러닝 데이터에 관심있는분들 : 네이버 블로그](https://blog.naver.com/kmh03214/221685090465)

- collections
    - deque
    - Counter

        파이썬의 기본 자료구조인 사전(dictionary)를 확장하고 있기 때문에, 사전에서 제공하는 API를 그대로 다 시용할 수가 있다. 각 개수 세서 dict 형태로 리턴

        ```python
        from collections import Counter

        Counter("hello world").most_common() #데이터의 개수가 많은 순으로 정렬된 배열을 리턴
        '''
        1. 이 메서드의 인자로 숫자 K를 넘기면 그 숫자 만큼만 리턴하기 때문에, 
        가장 개수가 많은 K개의 데이터를 얻을 수도 있다
        2. counter 인스턴스간 더하기, 빼기, 교집합, 합집합 등의 기능도 추가로 이용할 수 있다'''

        ```

        Counter('hello world').most_common()

- bisect

    파이썬에서 제공하는 표준 라이브러리. binary search 알고리즘을 이용해서 시퀀스를 검색하고, 시퀀스에 항목을 삽입할 수 있는 함수를 제공한다. 

    bisect.bisect(a, x, lo = 0, hi = len(a))

    bisect.bisect()는 bisect.bisect_right()와 동일

    bisect.bisect_left()는 x와 동일한 값이 시퀀스 a에 존재할 때 그 값 위치 리턴

    bisect.bisect_right()는 그 바로 뒤 위치 리턴

    bisect.insort(a,x,lo=0,hi=len(a))는 오름차순으로 정렬된 시퀀스에 x 삽입

    ```python
    import bisect

    sequence = [1, 3, 4, 5]

    print(bisect.bisect(sequence,1)) #1
    ```

- heapq

    ## **힙 자료구조**

    heapq 모듈은 이진 트리(binary tree) 기반의 최소 힙(min heap) 자료구조를 제공합니다. 자바에 익숙하신 분이라면 `PriorityQueue` 클래스를 생각하시면 이해가 쉬우실 것 같습니다.

    min heap을 사용하면 원소들이 항상 정렬된 상태로 추가되고 삭제되며, min heap에서 가장 작은값은 언제나 인덱스 0, 즉, 이진 트리의 루트에 위치합니다. 내부적으로 min heap 내의 모든 원소(k)는 항상 자식 원소들(2k+1, 2k+2) 보다 크기가 작거나 같도록 원소가 추가되고 삭제됩니다.

    ## **힙에 원소 추가 / 삭제**

    `heapq` 모듈의 `heappush()` 함수를 이용하여 힙에 원소를 추가할 수 있습니다. 첫번째 인자는 원소를 추가할 대상 리스트이며 두번째 인자는 추가할 원소를 넘깁니다.

    heapq 모듈의 heappop() 함수를 이용하여 힙에서 원소를 삭제할 수 있습니다. 원소를 삭제할 대상 리스트를 인자로 넘기면, 가장 작은 원소를 삭제 후에 그 값을 리턴합니다.

    ```python
    import heapq

    heap = []

    heapq.heappush(heap,4)
    heapq.heappush(heap,1)
    heapq.heappush(heap,7)
    heapq.heappush(heap,3)
    print(heap) #[1, 3, 7, 4]

    heapq.heappop(heap)
    ```

    ## 기존 리스트를 힙으로

    heapq.heapify(heap)

    여기서 주의사항은 인덱스 0에 가장 작은 원소가 있다고 해서, 인덱스 1에 두번째 작은 원소, 인덱스 2에 세번째 작은 원소가 있다는 보장은 없다는 것