def isWrongPhoneNumber(phoneNumber) :
    flag=str(phoneNumber).startswith("010")
    flag=(len(str(phoneNumber).split("-")) == 3) and flag
    flag=(len(str(phoneNumber))==13) and flag
    return not flag

def wrong_guest_book(book) :
    book = str(book).split('\n')
    for info in book :
        name, phone = info.split(',')
        if isWrongPhoneNumber(phone) : 
            print("잘못 쓴 사람 :", name)
            print("잘못 쓴 번호 :", phone)

guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""

wrong_guest_book(guest_book)