# 2020 KAKAO BLIND RECRUITMENT - 문자열 압축
def solution(s):
    answer = len(s)
    count = []
    index = 0
    tmp = 0
    short = 0
    
    print(answer)
    
    for i in range(1,(len(s)//2)+1) :
        short = len(s)
        tmp = 0
        count.clear()
        index = 0
        
        while(1):
            if(s[index:index+i] == s[index+i:index+i+i]) :
                tmp += 1
            else:
                if(tmp != 0):
                    count.append(tmp)
                tmp = 0
            
            if(index+i+i) > len(s) :
                break
            index += i
        
        for j in range(len(count)) :
            if(count[j]<9):
                short = short - ((count[j] + 1) * i - (i + 1))
            elif(count[j]>8) and (count[j] < 99):
                short = short - ((count[j] + 1) * i - (i + 2))
            elif(count[j]>98) and (count[j] < 998):
                short = short - ((count[j] + 1) * i - (i + 3))
            else:
                short = short - ((count[j] + 1) * i - (i + 4))
        if(short < answer) :
            answer = short
    
    return answer
