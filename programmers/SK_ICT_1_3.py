#SK ICT 3번문제
def solution(width, height, diagonals):
    answer = 0
    dots = []

    for i in range(len(diagonals)):
        dots.append([diagonals[i][0],diagonals[i][1]-1])
        dots.append([diagonals[i][0]-1,diagonals[i][1]])

    for i in range(0,len(dots),2) :
        tmp3 = 0
        tmp1 = grid(dots[i][0],dots[i][1])
        cache.clear()
        tmp2 = grid(width - dots[i+1][0], height - dots[i+1][1])
        cache.clear()
        tmp3 += (tmp1 * tmp2)

        tmp1 = grid(dots[i+1][0],dots[i+1][1])
        cache.clear()
        tmp2 = grid(width - dots[i][0], height - dots[i][1])
        cache.clear()
        tmp3 += (tmp1 * tmp2)
        answer += tmp3 % 10000019

    return answer

cache={}

def grid(r,c):
    if c==0 or r==0:
        return 1
    elif r==1:
        return c+1
    elif c==1:
        return r+1
    elif (r,c) in cache:
        return cache[r,c]
    else:
        cache[r,c]=grid(r,c-1)+grid(r-1,c) 
        return cache[r,c] 
