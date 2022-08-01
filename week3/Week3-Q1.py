
class gugudan :
    def __init__(self, number) :
        self.number = number
        self.oddEven = ''
    
    def getDan(self) :
        print(f"{self.number}단")
        
    def setOption(self, oddEven, min, max) :
        self.oddEven = oddEven
        self.min = min    
        self.max = max
    
    def __isOdd(self, value) :
        return (value % 2) != 0
    
    def printGGD(self) :
        for index in range(10) :
            result = int(self.number) * index
            
            if (self.oddEven == 'Odd') and (self.__isOdd(result)) :
                continue
            elif (self.oddEven == 'Even') and (not self.__isOdd(result)) :
                continue
            
            if (result >= self.min) and (result <= self.max) :
                print(f"{self.number} X {index} = {result}")
            
number = input("몇 단? :")
ggd = gugudan(number)
ggd.setOption('Odd', 0, 50)
ggd.printGGD()
