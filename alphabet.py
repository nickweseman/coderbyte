GAP = ord('z') - ord('a')

def LetterChanges(str):
    new_str = ""

    for c in str:
        newc = c

        if ord(c) == ord('z') or ord(c) == ord('Z'):
            newc = chr(ord(c) - GAP)
        elif (ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z')):
            newc = chr(ord(c) + 1).lower()

        if newc == 'a' or newc == 'e' or newc == 'i' or newc == 'o' or newc == 'u':
           newc = newc.upper()

        new_str += newc

    return new_str

# keep this function call here
print(LetterChanges("hello*3"))
print(LetterChanges("fun times!"))
print(LetterChanges("Argument goes here"))


