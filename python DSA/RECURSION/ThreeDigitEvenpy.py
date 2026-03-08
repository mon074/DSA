# digits = [0,2,1,3,1,3]
# digits = [2,2,8,8,2]
# digits = [3,7,5]


digits.sort()
first,second,third=0,0,0

fprev,sprev,tprev='a','a','a'

ans=[]

def ThreeEven(first,second,third):
    global fprev
    global sprev
    global tprev
    global ans
    global digits

    if first<len(digits):
        #first
        if digits[first]!=fprev:
            d = str(digits[first])
        else:
            return ThreeEven(first+1,second,third)

        #second
        if second<len(digits):
            if sprev!=digits[second] and second!=first:
                d += str(digits[second])
            else:
                tprev='a'
                return ThreeEven(first,second+1,0)
        else:
            fprev=digits[first]
            sprev='a'
            tprev='a'
            return ThreeEven(first+1,0,0)
        #third
        if third<len(digits):
            if tprev!=digits[third] and third!=first and third!=second:
                d+=str(digits[third])
                tprev=digits[third]
                if int(d)%2==0 and len(str(int(d)))>2:
                    ans.append(int(d))
                    
            # else:
                # tprev=digits[third]
            return ThreeEven(first,second,third+1)
        else:
            sprev=digits[second]
            tprev='a'
            return ThreeEven(first,second+1,0)
    else:
        return ans


print(ThreeEven(first,second,third))

[102,120,130,132,210,230,302,310,312,320]