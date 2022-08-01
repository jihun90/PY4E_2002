from abc import *
import random

class RCP(metaclass=ABCMeta) :
    def battle(self) : 
        pass
    def getString(self) :
        pass

class Scissors(RCP) :
    def battle(self, computer) :
        return {"가위" : "비김",
                "바위" : "패배",
                "보" : "승리"}[computer]
    
    def getString(self) :
        return "가위"

class Rock(RCP) :
    def battle(self, computer) :
        return {"가위" : "승리",
                "바위" : "비김",
                "보" : "패배"}[computer]
    
    def getString(self) :
        return "바위"
        
class Paper(RCP) :
    def battle(self, computer)  :
        return {"가위" : "패배",
                "바위" : "승리",
                "보" : "비김"}[computer]
    
    def getString(self) :
        return "보"

def getRandomRCP() :
    return random(0, 2)

def getRCPObject(input) :
    return {"가위" : Scissors(),
            "바위" : Rock(),
            "보" : Paper()
            }[input]
    
def getRCP(input) :
    return {0 : "가위",
            1 : "바위",
            2 : "보"
            }[input]

def rcp(input) :
    my = getRCPObject(input)
    print(f"나 : {my.getString()}")
    
    com = getRCP(random.randint(0, 2))
    print(f"com : {com}")
    
    return my.battle(com)

games = int(input("몇 판을 진행하시겠습니까? : "))

myWin=0
comWin=0
draw=0
index=0
while index < games :
    my = input("가위 바위 보?")
    if (my == '가위') or (my == '바위') or (my =='보') :
        index = index + 1
        
        result = rcp(my)
        print(f"{index}번째 판 ", end='')
        print(f"나의 {result}")
    
        if result == '승리' : myWin = myWin + 1
        elif result == '패배' : comWin = comWin + 1
        else : draw = draw + 1
        
    else :
        print("다시 입력하세요!!")    

print(f"나의 전적 {myWin}승 {draw}무 {comWin}패")
print(f"Com의 전적 {comWin}승 {draw}무 {myWin}패")

