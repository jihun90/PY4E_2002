# 📌Q3. 학생 이름과 점수를 입력하면 학점을 출력하는 학점 변환기를 만들어 봅시다.

# 이름과 점수, 학점 모두 출력하도록 해봅니다.

from mimetypes import init


class student :
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __isAPlus(self) :
        return self.score >= 95
    def __isA(self) :
        return self.score >= 90
    def __isBPlus(self) :
        return self.score >= 85
    def __isB(self) :
        return self.score >= 80
    def __isCPlus(self) :
        return self.score >= 75
    def __isC(self) :
        return self.score >= 65
    def __isDPlus(self) :
        return self.score >= 60
    def __isF(self) :
        return self.score < 60
    
    def getGrade(self) :
        if self.__isAPlus : return "A+"
        elif self.__isA : return "A"
        elif self.__isBPlus : return "B+"
        elif self.__isB : return "B"
        elif self.__isCPlus : return "C+"
        elif self.__isC : return "C"
        elif self.__isDPlus : return "D+"
        elif self.__isDPlus : return "D"
        elif self.__isF : return "F"
            

student1 = student("이호창", 99)
print(f"학생이름 : {student1.name}")
print(f"점수 : {student1.score}")
print(f"학점 : {student1.getGrade()}")