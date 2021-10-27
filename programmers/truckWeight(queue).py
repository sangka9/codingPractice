#스택/큐 - 다리를 지나는 트럭
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque(0 for i in range(bridge_length))
    waitingTruck = deque(truck_weights)
    sumOfWeights = waitingTruck.popleft()
    second = 1
    
    queue.popleft()
    queue.append(sumOfWeights)
    
    while (sumOfWeights > 0 or len(waitingTruck) > 0) :
        if len(waitingTruck) > 0 :
            if sumOfWeights - queue[0] + waitingTruck[0] <= weight :
                    queue.append(waitingTruck[0])
                    sumOfWeights = sumOfWeights - queue.popleft() + waitingTruck.popleft()
            else:
                queue.append(0)
                sumOfWeights -= queue.popleft()
        elif len(waitingTruck) == 0 and sumOfWeights > 0 :
                queue.append(0)
                sumOfWeights -= queue.popleft()
        
        second += 1
    
    return second
