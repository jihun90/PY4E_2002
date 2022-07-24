# Q3. 파이썬은 우리의 명령을 이해하지 못했을 때, 친절하게 Error Message를 통해
#      어떤 명령을 이해하지 못했는지 알려줍니다.  그것을 보고 코드의 버그를 수정해가는 과정을
#      Debugging이라고 합니다. 이것은 코딩에 있어서 매우 중요합니다.
#      따라서, Error Message에 대해서 이해하는 시간을 가져봅시다.
#      강의에서는 SyntaxError, ValueError, TypeError 3가지가 등장했습니다.
#     ①각각의 Error를 발생시키는 코드를 2가지씩 만들어보고
#     ②Debugging한 코드도 만들어 봅시다.
#     ③그리고 그 밖에 다른 Error도 3가지를 찾아 그 Error를 발생시키는 코드와
#     ④Debugging한 코드를 1가지씩 만들어 봅시다.

## SyntaxError
#print(:'Hello')

## ValueError
#int('Hello')

## TypeError
#temp = 'Hello' + 123

## indexError
#a = [1, 2, 3]
#a[4]

## ZeroDivision Error
#a = 5/0

## Indentation Error
#for i in range(5):
#print(i)
