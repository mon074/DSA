s = 'MCMXCIV'
roman = {"I": 1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
#print(roman[s[-1]])
def RomanToInt(arr,roman):
    i = len(arr)-1
    sum = roman[arr[-1]]
    while i>0:
        if roman[s[i]]>roman[s[i-1]]:
            sum = sum-roman[s[i-1]]
            i-=1
        else:
            sum = sum+roman[s[i-1]]
            i-=1
    return sum

answer = RomanToInt(s,roman)
print(answer)
    
