

from typing import Iterable


def grader(s, a) :
    dic = dict()
    for solution in s :
        name, answer = solution.split(',')    
        score = sum([10 for i in range(len(answer)) if int(answer[i]) == a[i]])
        dic[name] = score

    result = sorted(dic.items(), key=lambda x : x[1], reverse=True)
    
    for index, res in enumerate(result) :
        print(f"학생 : {res[0]} 점수 : {res[1]}점 {index+1}등")
        


# 학생 답
s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

# 정답지
a = [3,2,4,2,5,2,4,3,1,2]

grader(s, a)
