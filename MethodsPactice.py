import sys
from array import _array_reconstructor
from builtins import int, set


class Methods:

    def getAllindex(num):
        lst = []
        for i in num:
            lst.append(i)
        return lst

    def reverseString(text):
        result = ''
        for i in text:
            result = i + result
        return result

    def FactorialNum(num):
        result = 1
        for i in range(1, num + 1):
            result = i * result
        return result

    """Distance of two closet number"""

    def getDistance(arr):
        arr.sort()
        minN = arr[1] - arr[0]
        indexOne = 0
        indexTwo = 0
        maxIndex = len(arr) - 1
        for i in range(maxIndex):
            if minN > arr[i + 1] - arr[i]:
                minN = arr[i + 1] - arr[i]
                indexOne = i
                indexTwo = i + 1
        print("Closest value {} and {}".format(arr[indexOne], arr[indexTwo]))
        return minN

    def getPalindrome(text):
        str = ""
        for i in text:
            str = i + str
        if str == text:
            return True
        else:
            return False

    def reverseInteger(num):
        reverse = 0
        reminder = 0
        while num != 0:
            reminder = int(num % 10)
            reverse = int(reverse * 10 + reminder)
            num = int(num / 10)
        print(reverse)

    def sums(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            print('The sum of three numbers: ', a + b + c)
        elif a is not None and b is not None:
            print("The sum of 2 numbers: ", a + b)
        else:
            print("Please provide two or three arguments")

    # i can use any number of arguments for that methods
    def sum2(*a):
        total = 0;
        for i in a:
            total = total + i
        print(total)

    f = "User1,User2,user1,user3,user2,user3,user1"
    l = f.lower().split(',')
    m = {}
    for x in l:
        if x in m:
            m[x] += 1
        else:
            m[x] = 1
    print(m)

    def twoSum(nums, target):
        list = [0, 0]
        map = {}
        for i in range(len(nums)):
            if target - nums[i] not in map:
                map[nums[i]] = i
            else:
                list[1] = i
                list[0] = map.get(target - nums[i])
        return list

    def reverseArray(arr):
        reverseArray = []
        length = len(arr)
        for i in range(len(arr)):
            reverseArray.append(arr[length - i - 1])
        return reverseArray

    def getPrimeNumber(num):
        primeNumber = []
        for i in range(2, num):
            for j in range(2, num):
                if i == j:
                    primeNumber.append(j)
                if i % j == 0:
                    break
        return primeNumber

    def getDuplicate(text):
        str = ""
        map = {}
        for i in text:
            if i not in map:
                map[i] = 1
            else:
                map[i] = map.get(i) + 1
        for key, value in map.items():
            if value > 1:
                str = str + key
        return str

    def isNumPlaindrome(num):
        reverse = 0
        input = num
        while num != 0:
            reminder = int(num % 10)
            reverse = int(reverse * 10 + reminder)
            num = int(num / 10)
        if reverse == input:
            return True
        else:
            return False

    def getNearestPlaindrome(num):
        palindromNum = 0
        increase = 0
        decrese = 0
        while True:
            increase = increase + 1
            number = num + increase
            if Methods.isNumPlaindrome(number) == True:
                palindromNum = number
                return palindromNum
            else:
                decrese = decrese + 1
                number2 = num - decrese
                if Methods.isNumPlaindrome(number2) == True:
                    palindromNum = number2
                    return palindromNum

    def canBeConvertedPalindrome(text):
        map = {}
        for i in text:
            if i not in map:
                map[i] = 1
            else:
                map[i] = map.get(i) + 1
        blnFlag = False
        for key, value in map.items():
            if value % 2 == 1:
                if blnFlag:
                    return False
                else:
                    blnFlag = True
        return blnFlag

    def sumPairs(arr, target):
        map = {}
        for i in range(len(arr)):
            if target - arr[i] not in map:
                map[arr[i]] = i
            else:
                print(target - arr[i], ",", arr[i])
                continue

    def getDupFromArray(arr):
        duplicateValue = []
        map = {}
        for i in range(len(arr)):
            if arr[i] not in map:
                map[arr[i]] = 1
            else:
                map[arr[i]] = map.get(arr[i]) + 1
        for key, value in map.items():
            if value > 1:
                duplicateValue.append(key)
        return duplicateValue

    def getIntersectionOfTwoArray(arr1, arr2):
        set1 = set()
        set2 = set()
        for i in range(len(arr1)):
            set1.add(arr1[i])
        for j in range(len(arr2)):
            if arr2[j] in set1:
                set2.add(arr2[j])
        array = list(set2)
        return array

    def isAnagram(text1, text2):
        t1 = text1.lower().replace(" ", "")
        sort1 = sorted(t1)

        t2 = text2.lower().replace(" ", "")
        sort2 = sorted(t2)
        if sort1 == sort2:
            return True
        else:
            return False

    def binarySearch(arr, num):
        start = 0
        end = len(arr)
        while start <= end:
            mid = int((start + end) / 2)
            if num == arr[mid]:
                return mid
            elif num < arr[mid]:
                end = mid - 1
            elif num > arr[mid]:
                start = mid + 1
        return 0

    def longestSubStringNoRepeatedchar(text):
        longestTillNow = ""
        longestOverAll = ""
        set1 = set()
        for i in text:
            if i in set1:
                longestTillNow = ''
                set1.clear()
            longestTillNow = longestTillNow + i
            set1.add(i)
            if longestTillNow > longestOverAll:
                longestOverAll = longestTillNow
        return longestOverAll

    def mostCommonCharInString(text):
        map = {}
        s = text.lower().replace(" ", "")
        for i in s:
            if i not in map:
                map[i] = 1
            else:
                map[i] = map.get(i) + 1
        maxValue = 0
        maxChar = 0
        for key, value in map.items():
            if maxValue < value:
                maxValue = value
                maxChar = key
        return maxChar

    def maxRepeating(text):
        charCount = 1
        count = 0
        result = 0
        textLength = len(text)
        for i in range(textLength):
            if i < textLength - 1 and text[i] == text[i + 1]:
                charCount += 1
            else:
                if charCount > count:
                    count = charCount
                    result = text[i]
        return result

    def sumMaximumSubArray(arr):
        maxSoFar = -sys.maxsize - 1
        maxEndingHere = 0
        for i in arr:
            maxEndingHere = maxEndingHere + i
            if maxSoFar < maxEndingHere:
                maxSoFar = maxEndingHere
            if maxEndingHere < 0:
                maxEndingHere = 0;
        return maxSoFar

    def lengthOfLastWord(str) -> int:
        #   s = str.strip()
        lis = list(str.split(" "))
        if len(lis) == 0:
            return 0
        return len(lis[-1])

    def getPerfectNum(num):
        result = False
        total = 0
        for i in range(1, num - 1):
            if num % i == 0:
                total = total + i
        if total == num:
            result = True
        return result

    def reverseEachWord(str):
        reverseWord = ""
        list = str.split()
        for word in list:
            word = word[::-1]
            reverseWord = reverseWord + word + " "
        return reverseWord

    def moveAllZeroToRight(arr):
        newArra = []
        count = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1
        while count < len(arr):
            arr[count] = 0
            count += 1
            return arr

    def mergeArray(arr1, arr2):
        mergeArray = []
        index = 0
        for i in range(len(arr1)):
            mergeArray.append(arr1[i])
            index += 1
        for i in range(len(arr2)):
            mergeArray.append(arr2[i])
            mergeArray.sort()
        return mergeArray

    def getSecondLargetNum(arr):
        secondNum = -sys.maxsize - 1
        maxNum = -sys.maxsize - 1
        for i in range(len(arr)):
            if arr[i] > maxNum:
                secondNum = maxNum
                maxNum = arr[i]
            elif arr[i] > secondNum:
                secondNum = arr[i]
        return secondNum

    def getSeubStringWrepe(text):
        tillNow = ''
        str = ''
        s = set()
        for i in text:
            if i in s:
                s.clear()
                tillNow = ''
            tillNow = tillNow + i
            s.add(i)
            if len(tillNow) > len(str):
                str = tillNow
        return str

    def SumOfDigitsTillSingleDigitRecursion(num):
        if num < 9:
            return num
        sum = 0;
        while num > 0:
            sum = int(sum + num % 10)
            num = int(num / 10)
        if sum > 9:
            return Methods.findSum(sum)
        return sum

    def findSum(num):
        sum = 0;
        while num > 0:
            sum = int(sum + num % 10)
            num = int(num / 10)
        return sum

    def sumMaximumSubArray(arr):
        sum = -sys.maxsize - 1
        sum2 = 0
        for i in range(len(arr)):
            sum2 = sum2 + arr[i]
            if sum2 > sum:
                sum = sum2
            if sum2 < 0:
                sum2 = sum
        return sum

    def moveAllZeroToRight(arr):
        numList = []
        zero = []
        ind = 0
        for i in arr:
            if i > 0:
                numList.append(i)
            else:
                zero.append(0)
        numList.extend(zero)
        return numList

    def findFirstAndLastIndex(arr, target):
        list = [0, 0]
        indexOne = 0;
        indexTwo = 0
        map = {}
        for i in range(len(arr)):
            if arr[i] == target:
                if arr[i] in map:
                    map[arr[i]] = i
                    indexOne = i
                else:
                    map[arr[i]] = map.get(arr[i] + 1)
                    indexTwo = i
                if indexTwo == 0:
                    indexTwo = indexOne
        list[1] = indexOne
        list[0] = indexTwo
        return list;

    def thirdHighestNum(arr):
        max1 = -sys.maxsize - 1
        max2 = -sys.maxsize - 1
        max3 = -sys.maxsize - 1
        for i in arr:
            if i > max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i > max2:
                max3 = max2
                max2 = i
            elif i > max3:
                max3 = i
        return max3

    def findDisappearedNumber(arr):
        missNum = []
        numSet = set()
        for i in arr:
            numSet.add(i)
        for i in range(1, len(arr)):
            if i not in numSet:
                missNum.append(i)
        return missNum

    # Array partition
    def arraySumPair(arr):
        arr.sort()
        summ = 0
        for i in range(0, len(arr), 2):
            summ = summ + arr[i]
        return summ

    def smallerThenCurrent(arr):
        map = {}
        clone = arr.copy()
        arr.sort()
        for i in range(len(arr)):
            if arr[i] not in map:
                map[arr[i]] = i
        result = []
        for i in clone:
            result.append(map.get(i))
        return result

    def mostConsecutiveNum(arr):
        count = 0
        currCount = 1
        length = len(arr) - 1
        for i in range(length):
            if arr[i] == arr[i + 1]:
                currCount = currCount + 1
            else:
                if currCount > count:
                    count = currCount
                currCount = 1
        if currCount > count:
            count = currCount
        return count

    def sortestDistanceOfWord(text, str1, str2):
        array = text.split(' ')
        index1 = 0
        index2 = 0
        map = {}
        for i in range(len(array)):
            if array[i] not in map:
                map[array[i]] = 1
                if array[i] == str1:
                    index1 = i + 1
                elif array[i] == str2:
                    index2 = i + 1
                    break
            else:
                map[array[i]] = map.get(array[i]) + 1
                if array[i] == str2:
                    index2 = i + 1
        sortDis = index2 - index1
        if sortDis < 0:
            sortDis = index1 - index2
        return sortDis

    def longestContinuousIncreasingSubsequence(arr):
        longestOverAll = 0;
        longestTillNow = 0;
        length = len(arr) - 1
        for i in range(length):
            if arr[i] < arr[i + 1]:
                longestTillNow += 1
                longestOverAll = max(longestOverAll, longestTillNow)
            else:
                longestOverAll = 1
                longestTillNow = 0
        return longestOverAll


arrlcis = [1,3,5,4,7]
print("longestContinuousIncreasingSubsequence: ", Methods.longestContinuousIncreasingSubsequence(arrlcis))
print("sortestDistanceOfWord: ",
      Methods.sortestDistanceOfWord('practice makes perfect coding makes', 'practice', 'makes'))
arrmcn = [8,1,1,1,1,2,2,3]
print("mostConsecutiveNum: ", Methods.mostConsecutiveNum(arrmcn))
arrstc = [8, 1, 2, 2, 3]
print("smallerThenCurrent", Methods.smallerThenCurrent(arrstc))
sarr = [1, 4, 3, 2]
print(Methods.arraySumPair(sarr))

missNumfind = [4, 3, 2, 7, 8, 2, 3, 1]
print(Methods.findDisappearedNumber(missNumfind))
max3 = [2, 6, 7, 14, 9]
print(Methods.thirdHighestNum(max3))
arrFAL = [1, 3, 5, 5, 5, 5, 7, 67, 123, 125]
print(Methods.findFirstAndLastIndex(arrFAL, 5))
arr = [3, 5, 0, 3, 0, 3, 0]
print(Methods.moveAllZeroToRight(arr))
sumArray = [3, 5, -5, -1, 4, 3, -2]
print("sumMaximumSubArray: ", Methods.sumMaximumSubArray(sumArray))
print(Methods.SumOfDigitsTillSingleDigitRecursion(1234))
print(Methods.getSeubStringWrepe('pwwkert'))
xyz = [28, 3, 9, 44, 25]
print(Methods.getSecondLargetNum(xyz))
arx1 = [5, 3, 9, 1, 4, 11]
arx2 = [10, 0, 9, 6, 12, 11]
print(Methods.mergeArray(arx1, arx2))
moveZero = [2, 0, 3, 0, 8]
print(Methods.moveAllZeroToRight(moveZero))
print(Methods.reverseEachWord('hello world'))
print(Methods.getPerfectNum(496))
print("lengthOfLastWord: ", Methods.lengthOfLastWord("this is john"))
arraySum = [4, -2, -3, 4, -1, -2, 1, 5, -3]
print(Methods.sumMaximumSubArray(arraySum))
print(Methods.maxRepeating("aabbcceee"))
print("mostCommonCharInString: ",
      Methods.mostCommonCharInString("The Simple solution of this problem is to use two for loops"))
print("longestSubStringNoRepeatedchar: ", Methods.longestSubStringNoRepeatedchar("pwwkew"))
arrB = [2, 4, 5, 9, 10, 13, 15, 17]
print("binarySearch: ", Methods.binarySearch(arrB, 5))
print(Methods.isAnagram('Hello World', 'wold hello'))
arr1 = [4, 9, 5]
arr2 = [9, 4, 9, 8, 4]
print("getIntersectionOfTwoArray: ", Methods.getIntersectionOfTwoArray(arr1, arr2))
forDupArray = [4, 8, 3, 4, 9, 7, 9]
print("getDupFromArray: ", Methods.getDupFromArray(forDupArray))
arrayNum = [4, -2, 6, 7, 3, 5]
Methods.sumPairs(arrayNum, 10)
print(Methods.canBeConvertedPalindrome("mmmo"))
print(Methods.getNearestPlaindrome(118))
print("isNumPlaindrome: ", Methods.isNumPlaindrome(121))
print(Methods.getDuplicate("optimumo"))
print("getPrimeNumber: ", Methods.getPrimeNumber(10))
a = [1, 8, 3, 9]
print("reverseArray: ", Methods.reverseArray(a))
print('Two sum: ', Methods.twoSum(a, 12))
Methods.sum2(12, 30, 6)
print(Methods.sums(2, 5, 7))
print(Methods.reverseInteger(123))
print("getPalindrome: ", Methods.getPalindrome(('anaa')))
arrd = [25, 14, 1, 5, 6]
print(Methods.getDistance(arrd))
print("Factorial number:", Methods.FactorialNum(5))
print(Methods.reverseString("Automation"))
num = [1, 2, 3, 4]
print(Methods.getAllindex(num))
