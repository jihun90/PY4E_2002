
def isPrimeNumber(value) :
    for j in range(2, value) : 
            if (value % j) == 0 :
                return False
    return True

def count_prime_number(n, m) :
    return len([i for i in range(n, m+1) if isPrimeNumber(i)])
        
n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
print(f"소수개수 {count_prime_number(n, m)}")