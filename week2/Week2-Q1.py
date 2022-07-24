# 📌Q1. 컴퓨터와 함께하는 가위바위보 게임을 만들어봅시다!

# 조건1 : 함수의 인자로는 나의 가위바위보 선택이 들어감
#           (0, 1 ,2 혹은 "가위", "바위", "보" 로 입력할 수 있습니다. - 총 6가지 방법으로 넣을 수 있음)

# 조건2 : 누가 무엇을 냈고, 누가 승리 했는지 출력이 되어야 함

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
    
    print(f"나의 {my.battle(com)}")
    
my = input("가위 바위 보?")
rcp(my)


