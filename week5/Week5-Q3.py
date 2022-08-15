import random

def makeRandomNumbers() :
    setData = set()
    while (len(setData) < 3) :
        setData.add(random.randint(0,100))

    setData = sorted(setData)
    return setData

def isOverMin(dataList, value) :
    return int(min(dataList)) <= value

def isOverMax(dataList, value) :
    return int(max(dataList)) <= value

randomNumbers = makeRandomNumbers()
tempRandomNumbers = randomNumbers.copy()

index = 0
inputList = list()
isSolMin = False
isSolMax = False
while(len(randomNumbers)) :
    index += 1
    print(f"{index}차 시도")
    
    try :
        inValue = input("숫자를 예측해보세요 : ") 
        if(not inValue.isdigit()) : raise Exception("입력 오류 : 다시 입력하세요.")
    except Exception as e :
        print(e)
        index -= 1
        continue
    
    if int(inValue) in randomNumbers :
        result = ["최솟값", "중앙값", "최댓값"][tempRandomNumbers.index(int(inValue))]
        print(f"숫자를 맞추셨습니다! {inValue}는 {result}입니다.")
        if not isSolMin : isSolMin = "최솟값" == result
        if not isSolMax : isSolMax = "최댓값" == result
        randomNumbers.remove(int(inValue))
    elif int(inValue) in inputList :
        print("이미 예측에 사용한 숫자입니다")
        index-=1
        continue
    else :
        print(f"{inValue}는 없습니다.")
        if(index > 4) :
            if not isSolMin :
                if isOverMin(tempRandomNumbers, int(inValue)) : print(f"최솟값은 {inValue}보다 작습니다.")
                else : print(f"최솟값은 {inValue}보다 큽니다.")
            if not isSolMax :
                if isOverMax(tempRandomNumbers, int(inValue)) : print(f"최댓값은 {inValue}보다 작습니다.")
                else : print(f"최댓값은 {inValue}보다 큽니다")
        
    inputList.append(int(inValue))

print(f"{index}번 시도만에 예측 성공")