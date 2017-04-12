def LetterCapitalize(str):
    new_str = ""

    for s in str.split():
        new_str += s.capitalize() + " "

    return new_str


# keep this function call here
print(LetterCapitalize("hello world"))
print(LetterCapitalize("i ran there"))