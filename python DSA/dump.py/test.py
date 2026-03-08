s = "ab"
text = "abab"
print(len(text))
# code by chatgpt but using my logic it made little changes :D
i, j = 0, 0
index = []
char_count = {}
wins = len(s)  # Assuming 's' is a string you're comparing against

while j < len(text):
    # Add character from text[j] to the dictionary
    if text[j] in char_count:
        char_count[text[j]] += 1
    else:
        char_count[text[j]] = 1

    if j - i + 1 < wins:
        j += 1
    elif j - i + 1 == wins:
        # Check if character counts in 's' match 'char_count'
        match = True
        for character in s:
            if s.count(character) != char_count.get(character, 0):
                match = False
                break

        if match:
            index.append(i)

        # Remove the first character of the current window
        char_count[text[i]] -= 1
        if char_count[text[i]] == 0:
            del char_count[text[i]]

        # Move the window
        i += 1
        j += 1
print(index)
'''
count, i, j = 0, 0, 0
char_count = {}
wins = len(s)  # Assuming 's' is a string you're comparing against

while j < len(text):
    # Add character from text[j] to the dictionary
    if text[j] in char_count:
        char_count[text[j]] += 1
    else:
        char_count[text[j]] = 1

    if j - i + 1 < wins:
        j += 1
    elif j - i + 1 == wins:
        # Check if character counts in 's' match 'char_count'
        match = True
        for character in s:
            if s.count(character) != char_count.get(character, 0):
                match = False
                break

        if match:
            count += 1

        # Remove the first character of the current window
        char_count[text[i]] -= 1
        if char_count[text[i]] == 0:
            del char_count[text[i]]

        # Move the window
        i += 1
        j += 1

print(count)'''



     