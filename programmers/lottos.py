def solution(lottos, win_nums):
    answer = []
    count = 0
    tmp = 0
    ranking = [6, 6, 5, 4, 3, 2, 1]
    # 0의 갯수 세기(지워진 숫자)
    tmp = lottos.count(0)
    
    #로또 맞은 갯수 세기
    for i in range(6) :
        if(win_nums[i] in lottos) :
            count += 1;
            
    #등수 입력
    answer.append(ranking[count+tmp])
    answer.append(ranking[count])
    
    
    return answer
