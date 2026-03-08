'''class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longst = 0
        i = 0
        length = 0
        new = []
        for i in s:
            if len(s)==1:
                return 1
            if i in new:
                longst = max(length,longst)
                new = []
                new.append(i)
            else:
                new.append(i)
                length = len(new)
                longst = max(length,longst)
        return longst'''
s = "timetopractise"
t = "ttoc"

'''char = {}
# Step 1: Store frequency of characters in t
for c in t:
    if c in char:
        char[c] += 1
    else:
        char[c] = 1
current_count = {c: 0 for c in char}
print(char)
print(current_count)'''

n =int(input("write a number tp find cube: "))
cube = n**3
print(cube)