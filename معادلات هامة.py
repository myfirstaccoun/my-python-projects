import mouse
import keyboard

# arr defs
def equalArr(arr, dimensions = 1): # arr1 = arr2
    res = []

    i = 0
    while i < len(arr):
        if dimensions == 1:
            res.append(arr[i])
        else:
            res.append([])
            e = 0
            while e < len(arr[i]):
                if dimensions == 2:
                    res[i].append(arr[i][e])
                else:
                    res[i].append([])
                    f = 0
                    while f < len(arr[i][e]):
                        res[i][e].append(arr[i][e][f])
                        f += 1
                e += 1
        i += 1

    return res

def allIndexInArr(arr, item): # 1D arr=[10,20,30,40,30], item=30 ==> [2,4]
	allIndex = []
	
	i = 0
	while i < len(arr):
		if arr[i] == item:
			allIndex.append(i)
		i += 1
	
	return allIndex

def inArr(arr, item): # ==> True, False
	return item in arr

def onSide(arr, item, greater = 1, startFrom = 0): # 2D arr=[1,1,1,3,2,2,2,1,2,2], item=2, greater=1 ==> [ [4,5,6], [8,9] ] ==> [ indexArr ]
	finalArr = []
	onceArr = []
	
	i = startFrom
	while i < len(arr):
		if arr[i] == item:
			onceArr.append(i)
		else:
			if len(onceArr) > greater:
				finalArr.append(onceArr)
				
			onceArr = []
		i += 1
	
	if len(onceArr) > greater:
		finalArr.append(onceArr)
		onceArr = []
		
	return finalArr

def fillArr(arr, fill, fromNum = -1, toNum = -1): # arr=["⬜","⬜","⬜"], fill="🟩", from=0,to=1 ==> ["🟩","🟩","⬜"] #
	arr = equalArr(arr)
	
	if fromNum == -1:
		fromNum = 0
	if toNum == -1:
		toNum = len(arr)-1
	
	if fromNum < len(arr) and toNum < len(arr):
		i = fromNum
		while i < toNum+1:
			arr[i] = fill
			i += 1
	
	return arr

def removeFromArr(arr, index = -1, txt = "", minusOne = 0):
	newArr = []
	i = 0
	if (index > -1 and minusOne == 0) or (index <= -1 and minusOne != 0):
		while i < len(arr):
			if i != index%len(arr):
				newArr.append(arr[i])
			i += 1
	else:
		counter = 0
		while i < len(arr):
			if arr[i] != txt or (arr[i] == txt and counter == 1):
				newArr.append(arr[i])
		
			if counter == 0 and arr[i] == txt:
				counter = 1
			
			i += 1
		
	return newArr

def deleteDuplicatesInArr(arr, removeOriginalItem = 0, spicificItem = -1, item = None):
	arr = equalArr(arr)
	
	i = 0
	continu = 1
	while i < len(arr) and (spicificItem == -1 or (spicificItem != -1 and continu == 1)):
		allInd = []
		if spicificItem == -1:
			allInd = allIndexInArr(arr, arr[i])
		else:
			allInd = allIndexInArr(arr, item)
		
		if len(allInd) > 1:
			e = len(allInd)-1
			while e > 0:
				arr = removeFromArr(arr, allInd[e])
				if spicificItem != -1:
					continu = 0
				e -= 1
					
			if removeOriginalItem > 0:
				arr = removeFromArr(arr, allInd[0])
				i -= 1
					
		i += 1
			
	return arr

def sumArr(arr, fromNum = -1, toNum = -1): # arr=[1,2,3], fromNum=0, toNum=1 ==> 1+2 = 3
	sum = 0
	if fromNum > -1 and toNum > -1:
		toNum += 1
	elif fromNum > -1 and toNum < 0:
		toNum = len(arr)
	elif fromNum < 0 and toNum < 0:
		fromNum = 0
		toNum = len(arr)
		
	while fromNum < toNum:
		sum += arr[fromNum]
		fromNum += 1
	
	return sum

def minusArr(arr): # [1,4,5,8,7] ==> [3,1,3,-1]
	res = []

	i = 1
	while i < len(arr):
		res.append(arr[i] - arr[i-1])
		i += 1
	
	return res

def makeColumnArr(arr, column = 0): # convert column in 2D arr to arr
	arrLen = len(arr)
	columnArr = []

	i = 0
	while i < arrLen:
		if column < len(arr[i]): columnArr.append(arr[i][column])
		i += 1

	return columnArr

def convertRowToCol(arr, columnArr, column = 0): # Col ==> column, columnArr ==> row
    i = 0
    while i < len(columnArr):
        arr[i][column] = columnArr[i]
        i += 1
    
    return arr

def addArr(fromArr, toArr): # fromArr=[4,5,6], toArr=[1,2,3] ==> [1,2,3,4,5,6]
	toArr = equalArr(toArr)
	for x in fromArr:
		toArr.append(x)

	return toArr

def delArr(smallArr, bigArr): # smallArr = [4,5,6], bigArr=[1,2,3,4,5,6] ==> [1,2,3]
	smallArr = equalArr(smallArr)
	bigArr = equalArr(bigArr)

	for x in smallArr:
		if inArr(bigArr, x):
			bigArr = removeFromArr(bigArr, -1, x)
	
	return bigArr

def sliceArr(arr, fromNum = 0, toNum = 0): # arr=[10,20,30,40,50], fromNum=1, toNum=3 ==> [20,30,40]
    newArr = []

    i = fromNum
    while i <= toNum:
        newArr.append(arr[i])
        i += 1
    
    return newArr

def reverseArr(arr): # arr=[1,2,3] ==> [3,2,1]
    return arr[::-1]

def search2D(arr, item, column = 0): # ==> [index]
	res = []

	i = 0
	while i < len(arr):
		if arr[i][column] == item:
			res.append(i)
		i += 1

	return res

def convert2D(arr): # ==> 1D, convert 2D to 1D, arr=[ [1,2,3], [4,5,6], [7,8,9] ] ==> [1,2,3,4,5,6,7,8,9]
	newArr = []
	
	i = 0
	while i < len(arr):
		e = 0
		while e < len(arr[i]):
			newArr.append(arr[i][e])
			e += 1
		i += 1
	
	return newArr

def rotate2DArr(arr, numR = 1): # numR ==> num of right turns
    arr = equalArr(arr, 2)
    
    a = 0
    while a < numR:
        res = []

        i = 0
        while i < len(arr[0]):
            res.append(makeColumnArr(arr, i)[::-1])
            i += 1
        
        arr = res
        a += 1
    
    return arr

def replaceArr(text, replArr): # text = "hello word!", replArr = [ ["word", "world"], ["!", "."] ] ==> "hello world."
    i = 0
    while i < len(replArr):
        text = text.replace(replArr[i][0], replArr[i][1])
        i += 1

    return text

def insertInArr(arr, itemToInsert, itemIndex = 0, isMultiItems = 0): # arr=[1,3,4], itemToInsert=2 ==> [1,2,3,4]
    arr = equalArr(arr)
    res = []

    i = 0
    while i < len(arr):
        if i == itemIndex:
            if isMultiItems == 0: res.append(itemToInsert)
            elif "list" in str(type(itemToInsert)):
                e = 0
                while e < len(itemToInsert):
                    res.append(itemToInsert[e])
                    e += 1
        res.append(arr[i])
        i += 1

    return res

def convertTxt(text): # convert text to code, "5 + 7" ==> 12
    try:
        return eval(text)
    except Exception as e:
        print("حدث خطأ في التحويل:", e)
        return None

# text defs
def decodeNum(text): # r2 ==> ["r", 2]
    res = []
    tmp = ""
    nums = "0123456789"

    i = 0
    while i < len(text)-1:
        tmp += text[i]
        if text[i] not in nums:
            if text[i+1] in nums:
                res.append(tmp)
                tmp = ""
        else:
            if text[i+1] not in nums:
                res.append(int(tmp))
                tmp = ""
        i += 1

    tmp += text[i]
    if text[i] in nums: res.append(int(tmp))
    if text[i] not in nums: res.append(tmp)
    tmp = ""

    return res

def right(text, amount):
    return text[-amount:]

def left(text, amount):
    return text[:amount]

def mid(text, offset, amount):
    return text[offset:offset+amount]

# mouse defs
def getMousePosition(saveKey="g", breakKey="0"):
    all = []

    while True:
        if keyboard.is_pressed(saveKey):
            x = mouse.get_position()[0]
            y = mouse.get_position()[1]
            
            item = input("what is it?\n")
            all.append([ item, [x, y] ])

        if keyboard.is_pressed(breakKey):
            break

    print(all)
