"""
CONTENTS
#coordinates
#instructions
#manipulations
#links
#size
#summing
"""


"""
COORDINATES
"""
#make the coordinate lists: xList and yList
class CoordinateList: 
    def __init__(self, intNum):
        self.length = intNum
        self.list = [False] * (intNum + 1)

"""
lengthValue = 5
xList = CoordinateList(lengthValue).list
yList = CoordinateList(lengthValue).list
print("xList:", xList)
print("yList:", yList)
"""


"""
INSTRUCTIONS
# a few formatting and test functions are combined into a single function
"""
#puts the Instruction into the desired format
def iFormat(str):
    #replace
    strReplaceList = [("turn", ""), ("through", ""), (",", " ")] #replace useless strings
    for s in strReplaceList:
        str = str.replace(s[0], s[1])
    str = str.split() #turn it from string to list
    return str #this is now a list
    
#determines if the Instruction is valid
def iValid(iList):
    if len(iList) != 5: #all valid Instructions are of length 5
        return False
    if iList[0] not in ["off", "on", "switch"]: #all valid instructions begin with one of these Commands
        return False
    for i in range(1, 5, 1): # all valid instructions have four integer inputs
        try:
            if not isinstance(int(iList[i]), int):
                return False
            else:
                iList[i] = int(iList[i]) #convert entry to integer
        except ValueError:
            return False
    return True

#makes sure the integer values are within acceptable ranges
def iRange(iList, upperBound):
    for i in range(1, 5, 1):
        iList[i] = max(0, iList[i])
        iList[i] = min(iList[i], upperBound)
    return iList

#makes sure that x1<=x2 and y1<=y2
def iOrder(iList):
    return (int(iList[1]) <= int(iList[3]) and int(iList[2]) <= int(iList[4]))

#combines the Instruction functions into a single function
def iMake(str, upperBound): #input string from file, upperBound from file as int
    iList = iFormat(str) #format string into list
    if not iValid(iList): #check that the list has a valid form
        return ['pass', False, False, False, False]
    iList = iRange(iList, upperBound) #make sure that the range is within the bounds
    if not iOrder(iList): #check that the range is well ordered
        return ['pass', False, False, False, False]
    return iList
    
"""
made1 = "turn on 1,2 through 3,4"
made2 = "turn off 2,3 through 2, 3"
made3 = "switch 4,4 through 5,5"

made1 = iMake(made1, lengthValue)
made2 = iMake(made2, lengthValue)
made3 = iMake(made3, lengthValue)

print("")
print("iList 1:", made1)
print("iList 2:", made2)
print("iList 3:", made3)
"""


"""
MANIPULATIONS
"""
#generates the ranges for manipulation
def mRange(iList, mAxis): #list, str
    if mAxis == 'x':
        mOutput = range(iList[1], iList[3] + 1, 1)
    else:
        mOutput = range(iList[2], iList[4] + 1, 1)
    return mOutput

#manipulates the boolean values of xList and yList given information in iList
def mMain(iList, zList, mAxis): #list, list, str
    #command
    iCommand = iList[0]
    #check
    if iCommand == 'pass':
        return zList
    #range
    zRange = mRange(iList, mAxis)
    #manipulate booleans
    for z in zRange:
        if iCommand == "on":
            zList[z] = True
        elif iCommand == "off":
            zList[z] = False
        else:
            zList[z] = not bool(zList[z])
    return zList
        
"""        
xList = mMain(made3, xList, 'x')
print("")
print(xList)

yList = mMain(made3, yList, 'y')
print("")
print(yList)
"""


"""
LINKS
"""
import urllib.request
from urllib.error import URLError, HTTPError

#check if link is valid
def validLink(strLink): #str
    try:
        theLink = urllib.request.urlopen(strLink)
        return True
    except ValueError:
        return False
    except HTTPError:
        return False
    except URLError:
        return False
    else:
        return False

class CleanLink:
    
    def __init__(self, strLink):
        self.str = strLink
        self.clean = self.str.rstrip('\n')

"""
aLink = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
print("")
print(validLink(aLink))

bLink = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt\n"
print("")
print(bLink)
bLink = CleanLink(bLink).clean
print("")
print(bLink)
print("test line")
"""


"""
SIZE
"""
#makes it a clean string
def sRemoveLeftWhiteSpace(strInput): #str
    strInput = strInput.lstrip()
    strInput = strInput.lstrip('b')
    strInput
    
#checks if length is one i.e. only one number was given
def sCheckSize(strInput): #str
    return (len(strInput.split()) == 1) #boolean output

#checks if the entry is an integer
def sCheckInt(strInput): #str
    try:
        return isinstance(int(strInput), int)
    except ValueError:
        return False

#checks the range
def sCheckRange(strInput): #str
    theInt = int(strInput)
    return (theInt > -1) and (theInt < 10**9)


"""
SUMMING
"""
#change for On command
def sOn(iList, xList, yList):
    #z2 - z1 + 1
    x1 = iList[1]
    x2 = iList[3]
    y1 = iList[2]
    y2 = iList[4]
    xVar = x2 - x1 + 1
    yVar = y2 - y1 + 1
    #already on
    xOn = sum(xList[x1 : x2 + 1 : 1])
    yOn = sum(yList[y1 : y2 + 1 : 1])
    #output
    xVar += xOn
    yVar += yOn
    return xVar * yVar
    
#change for Off command
def sOff(iList, xList, yList):
    #z2 - z1 + 1
    x1 = iList[1]
    x2 = iList[3]
    y1 = iList[2]
    y2 = iList[4]
    xVar = x1 - x2 - 1
    yVar = y1 - y2 - 1
    #already off
    xOff = (x2 - x1 + 1) - sum(xList[x1 : x2 + 1 : 1])
    yOff = (y2 - y1 + 1) - sum(yList[y1 : y2 + 1 : 1])
    #output
    xVar += xOff
    yVar += yOff
    return xVar * yVar

#change for Switch command
def sSwitch(iList, xList, yList):
    return sOff(iList, xList, yList) - sOn(iList, xList, yList)

#change
def sSum(iList, xList, yList):
    theCommand = iList[0]
    if theCommand == 'on':
        return sOn(iList, xList, yList)
    if theCommand == 'off':
        return sOff(iList, xList, yList)
    if theCommand == 'switch':
        return sSwitch(iList, xList, yList)
    if theCommand == 'pass':
        return 0