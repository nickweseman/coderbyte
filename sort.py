def AlphabetSoup(str):
    new_str = ""
    for c in sorted(str):
        new_str += c

    return new_str


# keep this function call here
print(AlphabetSoup("coderbyte"))
print(AlphabetSoup("hooplah"))