def solution(new_id):
    answer = ''
    
    
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    possible = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-','_','.','0','1','2','3','4','5','6','7','8','9']
    
    #1단계
    for i in range(len(alphabet)) :
        new_id = new_id.replace(alphabet[i], chr(ord(alphabet[i])+32))
        
    #1단계 함수로 가능
    new_id = new_id.lower()
    
    tmp_id = list(new_id)
    #2단계 지정 문자 제외 제거
    for i in range(len(tmp_id)) :
        if(tmp_id[i] not in possible) :
            tmp_id[i] = "#"
    
    new_id = "".join(tmp_id)
    new_id = new_id.replace("#","")
    
    #3단계
    tmp_id = list(new_id)
    dot_list = []
    tmp = 0
    
    for i in range(len(tmp_id)-1):
        if(tmp_id[i] == '.') and (tmp_id[i+1] == '.') :
            dot_list.append(i+1)
    
    for i in range(len(dot_list)) :
        del tmp_id[dot_list[i] - tmp]
        tmp += 1

    #4단계
    if(tmp_id[0] == '.') and (len(tmp_id)>1):
        del tmp_id[0]
    if(tmp_id[-1] == '.') and (len(tmp_id)>1):
        del tmp_id[-1]
    if('.' in tmp_id) and (len(tmp_id) == 1) :
        del tmp_id[0]
        
    #5단계
    if(len(tmp_id) == 0) :
        tmp_id.append('a')
        
    #6단계
    if(len(tmp_id) > 15) :
        tmp_id = tmp_id[0:15]
        
    if(tmp_id[-1] == '.') :
        del tmp_id[-1]
        
    #7단계
    while(len(tmp_id) < 3):
        tmp_id.append(tmp_id[-1])
        
    answer = "".join(tmp_id)
    #print(answer)
        
    return answer
