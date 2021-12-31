# 코딩테스트 연습 - 해시 - 전화번호 목록
def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(1,len(phone_book),1) :
        if phone_book[i].startswith(phone_book[i-1]) :
            answer = False
            break
        
    return answer
