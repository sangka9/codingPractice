# Q1 Answer template

def solution(lottos, win_nums):
    best = 0 # max case
    worst = 0 # min case
    check = [0 for i in range(len(win_nums))] # win_nums 가 사용 유무 확인 / 사용 1 , 미사용 1
    
    for i in range(len(lottos)) :
        if lottos[i] == 0 : # 지워진 경우
            if sum(check) == len(win_nums) : # 더이상 맞출 번호가 없는 경우
                break
            else :
                check[check.index(0)] = 1 # 맞출 번호가 있는 경우
                best += 1
        else :
            if lottos[i] in win_nums : # 번호가 안지워지고 맞춘 경우
                best += 1
                worst += 1
                check[win_nums.index(lottos[i])] = 1
    
    #등수 확인
    if best <= 1 : best = 6
    else : best = 7 - best
    
    if worst <= 1 : worst = 6
    else : worst = 7 - worst
    
    return [best,worst]

lottos = [0, 0, 0, 0, 0, 0] #[44, 1, 0, 0, 31, 25]
win_nums = [38, 19, 20, 40, 15, 25] #[31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)

###################################################################################

# Q1 Answer template

def solution(lottos, win_nums):
    best = 0 # max case
    worst = 0 # min case
    
    erase = lottos.count(0)
    
    for i in range(len(lottos)) :
        if lottos[i] in win_nums : # 번호가 안지워지고 맞춘 경우
            best += 1
            worst += 1
    
    #등수 확인
    best += erase
    
    if best >= 7 : best = 1
    elif best <= 1 : best = 6
    else : best = 7 - best
    
    if worst >= 7 : worst = 1
    elif worst <= 1 : worst = 6
    else : worst = 7 - best
    
    return [best,worst]

lottos = [0, 0, 0, 0, 0, 0] #[44, 1, 0, 0, 31, 25]
win_nums = [38, 19, 20, 40, 15, 25] #[31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)

