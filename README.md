# Programmers-algorithm
1. 입국심사
2. 징검다리

## 1. [입국심사](https://programmers.co.kr/learn/courses/30/lessons/43238)
![image](https://user-images.githubusercontent.com/44918665/128691897-9fb5dfe3-5f6d-4308-9fb4-14906fa72c21.png)


### 1.1. 문제유형
- 이분탐색

### 1.2. 자료구조
- times (list): 심판관별 심사시간
- left, right (int): 최소 시간, 최대 시간
- mid (int): 정답으로 지정한 left, right의 중간값
- cnt (int): mid 시간안에 완료한 승객 수

### 1.3. 해결과정
1. 구하고자 하는 것은 최소 시간이다.
2. 이분탐색을 사용하여 정답 시간을 설정 후 지정한 시간안에 완료되는 지를 구한다.
3. left, right 지정 후 left <= right일 동안 다음 과정을 반복한다.
4. mid = (left+right)//2 중간값 지정 후, mid 시간안에 몇 명이 완료될 수 있는 지 계산한다.
5. cnt는 mid 시간을 times 별로 나눈 몫을 더한 값이다.

```python
def solution(n, times):
    answer = 0
    left, right = 0, min(times)*n

    while left<=right:
        mid = (left+right)//2
        cnt = 0
        for t in times:
            cnt += mid//t
        if cnt < n:
            left = mid+1
        else:
            right = mid-1
            answer = mid
    return answer
```

## 2. [징검다리](https://programmers.co.kr/learn/courses/30/lessons/43236)
![image](https://user-images.githubusercontent.com/44918665/128692613-1c462b48-ded1-4508-bde3-1ae5b3c5af16.png)

### 2.1. 문제유형
- 이분탐색

### 2.2. 자료구조
- distance (int): 목적지 거리
- rocks (list): 바위 위치를 저장한 리스트
- left, right (int): 바위별 거리의 최소값, 최대값
- mid (int): 정답으로 지정한 바위별거리. left, right의 중간값
- current (int): 현재 바위 위치
- diff (int): 현재 바위 위치를 기준으로 다음 바위까지의 거리
- cnt (int): 제거한 바위 수

### 2.3. 해결과정
- 최대 범위가 10억이므로 이분탐색을 위해 rocks를 정렬 후 시작한다.
1. 이분탐색을 지정하기 위해 최소, 최대거리를 지정한 후 mid를 계산한다.
2. mid가 정답이이라고 가정한 뒤, 제거한 바위 수가 n과 같은지 판단한다.
3. 바위를 하나씩 꺼내가며 diff를 계산하고, diff가 mid보다 작으면 cnt를 증가시킨다.
4. diff가 mid보다 크면 현재 바위를 rock으로 변경한다.
5. mid를 기준으로 계산한 cnt값이 n보다 크다면, 제거할 바위를 감소시켜야 하므로 right = mid-1
6. cnt값이 n보다 작거나 같다면, 바위를 더 줄여야 하므로 left = mid+1, answer = mid
7. 1-6 과정을 left <= right일 동안 반복한다.

```python
def solution(distance, rocks, n):
    answer = 0
    left, right = 0, distance
    rocks.sort()
    
    while left <= right:
        mid = (left+right)//2
        current, cnt = 0,0
        
        for rock in rocks:
            diff = rock - current
            if diff < mid:
                cnt += 1
            else:
                current=rock
        
        if cnt > n:
            right = mid-1
        else:
            left = mid+1
            answer = mid

    return answer
```
