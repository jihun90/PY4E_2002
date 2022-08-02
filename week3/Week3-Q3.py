
import numbers

n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
numbers = [i for i in range(n, m+1) if i % 2 == 0]
for i in numbers : 
    print(f"{i} 짝수")
    if(numbers.index(i) == round(len(numbers) / 2)) :
        print(f"{i} 중앙값")
