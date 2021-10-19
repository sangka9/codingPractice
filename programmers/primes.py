# Summer / Winter Coding (~2018) - 소수 만들기
def solution(nums):
    answer = 0

    nums.sort()
    board = []
    
    n = 3000
    a = [False,False] + [True]*(n-1)
    primes = []

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
    
    for i in range(len(nums) - 2) :
        for j in range(i + 1, len(nums) - 1) :
            for k in range(j + 1, len(nums)) :
                if((nums[i] + nums[j] + nums[k]) in primes) :
                    s = str(nums[i]) + ',' + str(nums[j])+ ',' + str(nums[k])
                    t = nums[i] + nums[j] + nums[k]
                    print('[' + s + ']를 이용해서' + str(t) + '을 만들 수 있습니다.')
                    answer += 1
                
                
    return answer
