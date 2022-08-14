from abc import *
import random


class bs31(metaclass=ABCMeta) :
    def __init__(self, name) :
        self.name = name
    
    def startTurn(self, curNum) :
        pass
        
class bs31User(bs31) :
    def __isDigit(self, dataList) :
        for data in dataList :
            if not data.isdigit() : return False
        return True    
    
    def __isContinuousNumber(self, curNum ,dataList) :
        for data in dataList :
            if curNum is not int(data) : return False
            curNum += 1
        return True

    def startTurn(self, curNum): 
        inData = input(f"{self.name} turn-숫자를 입력하세요 ")
        dataList = inData.split()
        
        if len(dataList) > 3 : raise Exception("입력은 3개까지만 입력이 가능합니다. 다시 입력해주세요")
        if not self.__isDigit(dataList) : raise Exception("숫자가 아닙니다. 다시 입력해주세요")
        if not self.__isContinuousNumber(curNum+1, dataList) : raise Exception("현재 숫자로 부터 연속된 숫자를 입력해주세요. 다시 입력해주세요.")
            
        curNum = dataList[-1]
        return int(curNum)
    
class bs31Com(bs31) :
    def startTurn(self, curNum):
        inCount = random.randint(1,3)
        comInput = [index + curNum for index in range(1,inCount+1) if(index + curNum) <= 31]
        [print("컴퓨터 : ", val) for val in comInput]
        
        return comInput[-1]
        


print('베스킨라빈스 써리원 게임')
print('------------------')

participantList = ["My" , "Computer"]

Me = bs31User("My")
Com = bs31Com("Com")

isWhoStart = random.randint(0, 1)
startTurn = participantList[isWhoStart]

targetTurn = {participantList[0] : Me, participantList[1] : Com}[startTurn]

curNumber = 0

while(curNumber < 31) :
    try :
        curNumber = targetTurn.startTurn(curNumber)
        print("현재 숫자 : ", curNumber)
    except Exception as e :
        print(e)
        continue
    
    lastUser = targetTurn.name

    isWhoStart = 1 - isWhoStart
    startTurn = participantList[isWhoStart]
    targetTurn = {participantList[0] : Me, participantList[1] : Com}[startTurn]
    
print(f"{lastUser} 탈락!!!!!!")
print("베스킨라빈스31 게임 끝!!!!!!!!!!!!")
print('-------------------------------')
