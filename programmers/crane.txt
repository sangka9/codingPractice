# 카카오 2019 카카오 개발자 겨울 인턴십 코딩 테스트 - 크레인 인형뽑기 게임
def solution(board, moves):
    answer = 0
    box = []
    recent = 0
    
    for i in range(len(moves)) :
        index = (moves[i] - 1)
        
        for j in range(len(board[0])) :
            if(board[j][index] != 0) :
                if(len(box) > 0) :
                    if(box[len(box)-1] == board[j][index]) :
                        answer += 2
                        box.pop()
                        board[j][index] = 0
                        break
                
                box.append(board[j][index])
                board[j][index] = 0
                break

    
    return answer
