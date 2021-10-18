# 2018 KAKAO BLIND RECRUITMENT - [1차] 비밀지도
def solution(n, arr1, arr2):
    answer = []
    board1 = []
    board2 = []    
    
    for i in range(n) :
        board1.append(binary(arr1[i], n))
        board2.append(binary(arr2[i], n))
    
        tmp = ""
        for j in range(n) :
            if(board1[i][j] or board2[i][j]) :
                tmp = tmp + "#"
            else :
                tmp = tmp + " "
        
        answer.append(tmp)
    
    return answer


def binary(n, length) :
    bi = []
    
    while(length) :
        bi.append(n % 2)
        n = n // 2
        length = length - 1
    
    bi.reverse()
    
    return bi
