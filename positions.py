def SimpleSymbols(str):
    str = str.lower()

    for i in range(0, len(str)):
        if ord('a') <= ord(str[i]) <= ord('z'):
            if i == 0 or i == len(str)-1:
                return "false"
            if str[i-1] != "+" or str[i+1] != "+":
                return "false"
    return "true"

# keep this function call here
print(SimpleSymbols("+d+=3=+s+"))
print(SimpleSymbols("f++d+"))