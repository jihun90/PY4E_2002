class member :
    def __init__(self, id, age, phone, gender, adress, count) :
        self.id = id
        self.age = age
        self._phone = phone
        self.gender = gender
        self.adress = adress
        self.count = count
        
    @property
    def phone(self) :
        return [self._phone, '000-0000-0000'][self._phone == 'x']
    
    def print(self) :
        print(f"아이디:{self.id}, 나이:{self.age}, 전화번호:{self.phone}, 성별:{self.gender}, 지역:{self.adress}, 구매횟수: {self.count}")
        

def good_customer(info) :        
    memberList = list()
    while (info is not '') :
        infoList = info.split(',', 6)
        
        if(len(infoList) > 6) : info = infoList[6]
        else : info = ''
        
        temp = member(infoList[0], infoList[1], infoList[2], infoList[3], infoList[4], infoList[5])
        memberList.append(temp)
    
    id = [m.id for m in memberList]
    age = [m.age for m in memberList]
    phone = [m.phone for m in memberList]
    gender = [m.gender for m in memberList]
    adress = [m.adress for m in memberList]
    count = [m.count for m in memberList]
    
    print("아이디 : ", end='')
    print(", " .join(id))
    print("나이 : ", end='')
    print(", " .join(age))
    print("전화번호 : ", end='')
    print(", " .join(phone))
    print("성별 : ", end='')
    print(", " .join(gender))
    print("adress : ", end='')
    print(", " .join(adress))
    print("구매횟수 : ", end='')
    print(", " .join(count))
    
    vip = [m for m in memberList if ((int(m.count) >= 8) and (m.phone != '000-0000-0000'))]
    for m in vip : 
        print("할인 쿠폰을 받을 회원정보 ", end="")
        m.print()

# 6명의 회원이고 "아이디,나이,전화번호,성별,지역,구매횟수" 순서로 입력되어 있음
info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"    
good_customer(info)
