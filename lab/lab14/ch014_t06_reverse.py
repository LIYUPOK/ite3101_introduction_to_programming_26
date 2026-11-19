def reverse(text:str)->str:
    word = ""
    length = len(test)
    for i in range(length - 1, -1, -1):
        word += test[i]
    return word