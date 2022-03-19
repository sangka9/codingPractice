#SK ICT 2차 2번 문제
def solution(arr, processes):
    answer = []
    time = 0
    active = []
    wait = []
    writeCount = 0

    while 1 :
        # 초가 맞으면 작업 스케줄에 넣기
        if len(processes) > 0:
            if int(processes[0].split()[1]) == time:
                if processes[0].split()[0] == "write":
                    writeCount += 1
                    # 동시에 시작 인 경우 우선순위 정하기 위해 wait 에 일단 저장
                    # active 또는 wait 에 write 있는 경우 무조건 저장
                wait.append(processes[0])
                processes.pop(0)

        if len(active) > 0:
            if active[0].split()[0] == "read":
                if writeCount == 0:  # wait 에 write process 가 없는 경우 read
                    for i in range(len(wait)):
                        active.append(wait[i])
                        active[-1] += " " + str(int(wait[i].split()[2]) + time)
                        wait.pop(i)

                deleteActive = []
                for i in range(len(active)):  # for 문인 이유는 다중 read 때문에
                    if int(active[i].split()[5]) == time:
                        start = int(active[i].split()[3])
                        end = int(active[i].split()[4])
                        arrString = ""
                        for j in range(start, end+1):
                            arrString += arr[j]
                        answer.append(arrString)
                        deleteActive.append(i)
                for i in range(len(deleteActive)) :
                    active.pop(deleteActive[i])

            elif active[0].split()[0] == "write":
                if int(active[0].split()[6]) == time:
                    start = int(active[0].split()[3])
                    end = int(active[0].split()[4])
                    changeStr = active[0].split()[5]
                    for j in range(start, end+1):
                        arr[j] = changeStr
                    writeCount -= 1
                    active.pop()

        if len(active) == 0:
            if writeCount == 0 and len(wait) > 0:  # wait 에 write process 가 없는 경우 read
                for i in range(len(wait)):
                    active.append(wait[i])
                    active[i] += " " + str(int(wait[i].split()[2]) + time)
                wait.clear()
            else:
                for i in range(len(wait)):  # write
                    if wait[i].split()[0] == "write":
                        active.append(wait[i])
                        active[-1] += " " + str(int(wait[i].split()[2]) + time)
                        wait.pop(i)
                        break


        print(f'time {time}')
        print(f'{active} / {wait}')

        if len(processes) == 0 and len(active) == 0 and len(wait) == 0:
            answer.append(time-1)
            break
        else:
            time += 1

    return answer


arr = ["1", "2", "4", "3", "3", "4", "1", "5"]
processes = ["read 1 3 1 2", "read 2 6 4 7", "write 4 3 3 5 2", "read 5 2 2 5", "write 6 1 3 3 9", "read 9 1 0 7"]
print(solution(arr, processes))
