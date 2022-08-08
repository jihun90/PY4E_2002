
def make_common(number) :
    result = ''
    for index, value in enumerate(reversed(str(number))) :
        index += 1
        result += value
        if ((index % 3) == 0) :
            result += ','
    
    result = result[::-1]
    if result[0] == ',' :
        result = result [1:]
    print(result)

make_common(9877998000)
        
            