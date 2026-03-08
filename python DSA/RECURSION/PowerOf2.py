x=0
n=5
def rec(x):
    power = 2**x

    if power == n:
        return True
    elif power > n:
        return False
    

    return rec(x+1)

print(rec(x))