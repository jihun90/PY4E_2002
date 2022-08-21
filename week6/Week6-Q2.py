import numpy

def isInterview(score) :
    return float(score) <= 3

def isBonus(socore) :
    return float(socore) >= 5

def sales_management(names, records) :
    info = dict(zip(names, records))
    info = {name : numpy.mean(score) for name, score in info.items()}
    info = sorted(info.items(), key=lambda x : x[1], reverse=True)
    info = list(info)
    
    if isBonus(info[0][1]) : print("보너스 대상자 ", info[0][0])
    if isBonus(info[1][1]) : print("보너스 대상자 ", info[1][0])
    
    print("")
    
    if isInterview(info[4][1]) : print("면담 대상자 ", info[4][0])
    if isInterview(info[5][1]) : print("면담 대상자 ", info[5][0])
        
    return info

# 이름, 실적
member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2], 
           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]

sales_management(member_names, member_records)