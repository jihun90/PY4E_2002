# 📌Q4. 나이와 현금 또는 카드를 입력하면 버스 요금이 출력되는 버스 요금 계산기를 만들어봅시다. 



class BusFare :
    def __init__(self, age, type) :
        self.age = age
        self.type = type
    
    def __isCard(self) :
        return self.type == "카드"
    
    def __isUnderAge8(self) :
        return self.age < 8
    def __isUnderAge14(self) :
        return self.age < 14
    def __isUnderAge20(self) :
        return self.age < 20
    def __isOver20(self) :
        return self.age >= 20
    def __isOver75(self) : 
        return self.age >= 75
    
    def getBusFare(self) :
        if self.__isUnderAge8() : return "무료"
        elif self.__isUnderAge14() : return ("450원", "450원")[not self.__isCard()]
        elif self.__isUnderAge20() : return ("720원", "1000원")[not self.__isCard()]
        elif self.__isOver20() : return ("1200원", "1300원")[not self.__isCard()]
        elif self.__isOver75() :  return "무료"
        
    def printAge(self) :
        print(f"나이 : {self.age}")
    def printType(self) :
        print(f"지불타입 : {self.type}")
    def printFare(self) :
        print(f"버스요금 : {self.getBusFare()}" )
    

#카드가 아니면 무조건 현금!
busFare1 = BusFare(30, "카드")
busFare1.printAge()
busFare1.printType()
busFare1.printFare()


