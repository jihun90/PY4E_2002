import datetime

def after_100(year, month, day) :
    cur = datetime.date(year, month, day)
    days = datetime.timedelta(days=100)
    after100days = cur + days
    curStr= cur.strftime("%y년 %m월 %d일 %a")
    after100Str = after100days.strftime("%y년 %m월 %d일 %a")
    print(f"{curStr}부터 100일 뒤는 {after100Str}")
    
after_100(2022, 8, 19)