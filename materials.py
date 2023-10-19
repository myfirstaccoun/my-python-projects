# CO2 ==> ["C", "O2"], MgO ==> ["Mg", "O"]

def split(text, delimiter = ""):
    arr = []

    if delimiter != "":
        tmp = ""

        i = 0
        while i < len(text):
            if text[i] != delimiter:
                tmp += text[i]
            elif tmp != "":
                arr.append(tmp)
                tmp = ""
            i += 1
        
        if tmp != "":
            arr.append(tmp)
    else:
        for x in text:
            arr.append(x)
    
    return arr
    
def convertTxt(text): # "3 + 2" ==> 5
    try:
        return eval(text)
    except Exception as e:
        print("حدث خطأ في التحويل:", e)
        return None

def filterArr(arr, filter="", mood="merge"):
    # filter Keywords ==> i = item, low = lowerCase, up = upperCase, >, >=, <, <=, =, && = and, || = or
    # mood = merge = arr of arrs || oneArr
    filter = "".join(filter.split())
    filters = split(filter, ["&&", "||"])
    print(filters)

    if mood == "merge":
        i = 0
        while i < len(arr):
            
            i += 1

    return ""

def replaceArr(text, replArr): # text = "hello word!", replArr = [ ["word", "world"], ["!", "."] ] ==> "hello world."
    i = 0
    while i < len(replArr):
        text = text.replace(replArr[i][0], replArr[i][1])
        i += 1

    return text

def materials(text, filter="text[itemNum+1].islower() or text[itemNum+1] in nums", filter_else_if="text[itemNum+1].isupper()"):
    text = split(text)
    arr = []
    tmp = ""
    nums = "123456789"
    tmpFilter = filter
    tmpElseFilter = filter_else_if

    i = 0
    while i < len(text)-1:
        replaceWords = [["itemNum", str(i)], ["text", str(text)], ["nums", f'"{str(nums)}"']]
        filter = replaceArr(filter, replaceWords)
        filter_else_if = replaceArr(filter_else_if, replaceWords)

        if convertTxt(filter):
            tmp += text[i]
        elif convertTxt(filter_else_if):
            tmp += text[i]
            arr.append(tmp)
            tmp = ""

        filter = tmpFilter
        filter_else_if = tmpElseFilter
        i += 1

    filter = replaceArr(filter, replaceWords)
    if convertTxt(filter):
        tmp += text[i]
    else:
        tmp = text[i]

    arr.append(tmp)
    tmp = ""
    return arr



print(materials("Ag2MoO4"))
