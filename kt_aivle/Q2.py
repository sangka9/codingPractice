# Q2 Answer template

N = int(input()) # 입력받는 숫자

def cycle(origin) :
    cnt = 0 # 카운트하는 숫자
    n = origin # 앞 선 숫자
    
    while 1 : # 사이클 카운트
        tmp = (n // 10) + (n % 10) # 첫번째와 두번째 자릿수 합
        n = (n % 10) * 10 + (tmp % 10) # 새로운 수 만들기
        #print(n, end=' ') #숫자 확인
        cnt += 1 # 카운트
        
        if n == origin : # 사이클이 완성 된 경우 break
            break
    
    #print()
    return cnt # 카운트 값 반환

count = cycle(int(N))

print(count)
