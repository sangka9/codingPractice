#2020 카카오 인턴십 - 키패드 누르기
def solution(numbers, hand):
    answer = ''
    rHand = 12
    lHand = 10
    lDistance = 0
    rDistance = 0
    
    middle = [[0, 4, 3, 4, 3, 2, 3, 2, 1, 2, 1, 0, 1],
              1, [3, 1, 0, 1, 2, 1, 2, 3, 2, 3, 4, 2, 4],
              3, 4, [2, 2, 1, 2, 1, 0, 1, 2, 1, 2, 3, 2, 3],
              6, 7, [1, 3, 2, 3, 2, 1, 2, 1, 0, 1, 2, 1, 2]]
    
    
    for i in range(len(numbers)) :
        if(numbers[i] == 1) or (numbers[i] == 4) or (numbers[i] == 7) :
            lHand = numbers[i]
            answer = answer + 'L'
        elif(numbers[i] == 3) or (numbers[i] == 6) or (numbers[i] == 9) :
            rHand = numbers[i]
            answer = answer + 'R'
        else :
            lDistance = middle[numbers[i]][lHand]
            rDistance = middle[numbers[i]][rHand]
            
            if(lDistance < rDistance) :
                lHand = numbers[i]
                answer = answer + 'L'
            elif(lDistance > rDistance) :
                rHand = numbers[i]
                answer = answer + 'R'
            else :
                if(hand == 'left') :
                    lHand = numbers[i]
                    answer = answer + 'L'
                else :
                    rHand = numbers[i]
                    answer = answer + 'R'
    
    print(answer)
    
    return answer
