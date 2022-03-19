#SK ICT 2번문제 바람개비 
def solution(n, clockwise):
    answer = [[0]*n for i in range(n)]

    if clockwise == True :
        if n == 1 :
            answer = [[1]]
        elif n == 2 :
            answer = [[1,2],[2,1]]
        elif n%2 == 0 : # 짝수
            number = 1
            plus = 0
            minus = 0
            i = 0
            j = 0
            while 1 :
                if answer[i][plus+j] == 0 :
                    answer[i][plus+j] = answer[plus+i][n-1-j] = answer[n-1-minus-i][j] = answer[n-1-i][n-1-j-minus] = number
                    number += 1
                    plus += 1
                    minus += 1

                    if i == n / 2 - 1 :
                        break
                else :
                    i += 1
                    j += 1
                    plus = 0
                    minus = 0

        elif n%2 == 1 : # 홀수
            number = 1
            plus = 0
            minus = 0
            i = 0
            j = 0
            while 1 :
                if answer[i][plus+j] == 0 :
                    answer[i][plus+j] = answer[plus+i][n-1-j] = answer[n-1-minus-i][j] = answer[n-1-i][n-1-j-minus] = number
                    number += 1
                    plus += 1
                    minus += 1
                else :
                    i += 1
                    j += 1
                    plus = 0
                    minus = 0

                    if i == n//2 :
                        answer[i][i] = number
                        break

    elif clockwise == False :
        if n == 1 :
            answer = [[1]]
        elif n == 2 :
            answer = [[2,1],[1,2]]
        elif n%2 == 0 : # 짝수
            number = 1
            plus = 0
            minus = 0
            i = 0
            j = 0
            while 1 :
                if answer[plus+i][j] == 0 :
                    answer[plus+i][j] = answer[i][n-1-minus-j] = answer[n-1-i][plus+j] = answer[n-1-minus-i][n-1-j] = number
                    number += 1
                    plus += 1
                    minus += 1

                    if i == n / 2 - 1 :
                        break
                else :
                    i += 1
                    j += 1
                    plus = 0
                    minus = 0

        elif n%2 == 1 : # 홀수
            number = 1
            plus = 0
            minus = 0
            i = 0
            j = 0
            while 1 :
                if answer[plus+i][j] == 0 :
                    answer[plus+i][j] = answer[i][n-1-minus-j] = answer[n-1-i][plus+j] = answer[n-1-minus-i][n-1-j] = number
                    number += 1
                    plus += 1
                    minus += 1
                else :
                    i += 1
                    j += 1
                    plus = 0
                    minus = 0

                    if i == n//2 :
                        answer[i][i] = number
                        break


    return answer
