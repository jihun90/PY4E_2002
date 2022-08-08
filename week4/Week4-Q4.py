class IdNumber :
    def __init__(self, idNumber) :
        temp = str(idNumber).split("-")
        if ((len(str(idNumber)) != 14) or (len(temp) != 2)) :
            raise Exception("잘못된 번호입니다.\n올바른 번호를 넣어주세요.")
        
        self.year = str(temp[0])[:2]
        tempGender = int(str(temp[1])[0])
        if (int(self.year) in range(0,22)): 
            isOver2000 = input("2000년 이후 출생자 입니까? 맞으면 o 아니면 x")
            if isOver2000 == 'o' :
                self.gender = {3:"남자", 4:"여자"}.get(int(tempGender), "Error")
            else :
                self.gender = "Error"
        else : 
            self.gender = {1:"남자", 2:"여자"}.get(int(tempGender), "Error")
            
        if (self.gender == "Error") : 
                raise Exception("잘못된 번호입니다.\n올바른 번호를 넣어주세요.")
        self.month = str(temp[0])[2:4]
    
    def getInfo(self) :
        print(f"{self.year}년 {self.month}월 {self.gender}")        
            
a = "500629-2222222"
try :
    idNumber = IdNumber(a)
    idNumber.getInfo()
except Exception as e :
    print(e)
    
    