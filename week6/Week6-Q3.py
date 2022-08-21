
stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]

stockList = stocks.split(',')
stockDict = {stock.split("/")[0] : 100 * ((sells[index] / float(stock.split("/")[2])) - 1) for index, stock in enumerate(stockList)}
sortedDict = sorted(stockDict.items(), key=lambda x : x[1], reverse=True)

for stock in sortedDict : print(f"{stock[0]}의 수익률 {stock[1]:.3}")