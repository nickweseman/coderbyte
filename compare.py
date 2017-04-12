def CheckNums(num1, num2):
    if num1 == num2:
        return -1
    else:
        return "true" if num2 > num1 else "false"

# keep this function call here
print(CheckNums(3, 122))
print(CheckNums(67, 67))