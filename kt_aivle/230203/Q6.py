# Q6 Answer template

def solution(arr):
    
    arr.pop(arr.index(min(arr)))
    
    if len(arr) == 0 :
        return -1
    else :
        return arr

arr = [4, 3, 2, 1] # [10]
answer = solution(arr)
print(answer)
