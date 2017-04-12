def FirstReverse(str):
    reversed_str = ""

    for i in range(len(str)):
        reversed_str += str[len(str) - i - 1]

    return reversed_str


def cheat_reverse(str):
    reversed_str = ""

    for c in reversed(str):
        reversed_str += c

    return reversed_str

def didnt_reverse(str):
    reversed_str = ""

    for c in str[::-1]:
        reversed_str += c

    return reversed_str


# keep this function call here
print(didnt_reverse("coderbyte"))
print(didnt_reverse("I Love Code"))

