
i = len(digits)-1
while i >= 0:
    if digits[i] < 9:
        digits[i] += 1
        break
    else:
        if i==0:
            digits[i] = 1
            digits.append(0)
            break
        else:
            digits[i] = 0
            i-=1
print(digits)
        

