# 스택/큐 - 기능개발
# 1번 풀이 O(n) = n^2
def solution(progresses, speeds):
    answer = []
    
    while len(progresses) > 0 :
        for i in range(len(progresses)) :
            if(progresses[i] < 100) :
                progresses[i] += speeds[i]
            else :
                progresses[i] = 100
        tmp = 0
        for i in range(len(progresses)) :
            if(progresses[i] >= 100) :
                tmp += 1
            else :
                break
        if(tmp > 0) :
            progresses = progresses[tmp:]
            speeds = speeds[tmp:]
            answer.append(tmp)
            
    return answer
  
  # 2번 풀이 O(n) = n 
  # 음수 반올림 -((progresses[i] - 100) // speeds[i])
  def solution(progresses, speeds):
    answer = []
    day = []
    
    for i in range(len(progresses)) :
        day.append(-((progresses[i] - 100) // speeds[i]))
        
    dDay = day[0]
    task = 1
    
    for i in range(1,len(day)) :
        if(dDay < day[i]) :
            answer.append(task)
            task = 1
            dDay = day[i]
        else :
            task += 1
    answer.append(task)
            
    return answer
