# Q4 Answer Template
data = input('숫자로 이루어진 문자열을 입력하세요. ')
result = 0 # 결과 저장 변수

for i in range(len(data)) :
    if i == 0 : # 첫번째 자리 수
        print(f'{data[i]} ',end = '')
        result += int(data[i])
    else :
        if int(data[i-1]) < 2 or int(data[i]) < 2 : # 앞뒤의 자리 수가 0 또는 1 일 경우 덧셈
            print(f'+ {data[i]} ',end = '')
            result += int(data[i])
        else : # 앞의 자리 수가 0 또는 1이 아닌 경우 곱셈
            print(f'* {data[i]} ',end = '')
            result *= int(data[i])
    
    if i == len(data) - 1 : # 마지막 자리 수까지 한 경우 = 출력
        print('= ',end = '')
        
print(result) # 결과값 출력
