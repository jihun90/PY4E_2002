# 📌Q2. 월급을 입력하면 연봉을 계산해주는 계산기를 만들어 봅시다. 세전 연봉과 세후 연봉을 함께 출력하도록 해봅니다.

def getTaxRate(salary) :
    if(salary <= 1200) :
        return 0.06
    elif(salary <= 4600) :
        return 0.15
    elif(salary <= 8800) :
        return 0.24
    elif(salary <= 15000) :
        return 0.35
    elif(salary <= 30000) :
        return 0.38
    elif(salary <= 50000) :
        return 0.40
    else :
        return 0.42
    
def calcTax(taxRate, salary) : 
    return taxRate * salary
    
monthly_payment =  input("당신의 월급은?(만원단위)")
salary = int(monthly_payment) * 12

print(f"세전연봉 : {salary}만원")
taxRate = getTaxRate(int(salary))
tax = float(calcTax(taxRate, salary))
print(f"세후연봉 {int(salary - tax)}만원")
    