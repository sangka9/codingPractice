# Summer/Winter Coding(~2018) - 스킬트리
def solution(skill, skill_trees):
    answer = 0
    ok = 1
    
    for i in range(len(skill_trees)):
        findOrder = list(skill_trees[i])
        findSkill = list(skill)
        ok = 1
        
        for j in range(len(findOrder)) :
            if(len(findSkill) == 0) or (ok == 0):
                break
            elif(findSkill[0] == findOrder[j]):
                del findSkill[0]
            else:
                for k in range(1,len(findSkill)):
                    if(findSkill[k] == findOrder[j]) :
                        findSkill.clear()
                        ok = 0
                        break
        answer += ok
    
    return answer
