def reverse(text:str)->str:
    word = ""
    length = len(text)
    for i in range(length - 1, -1, -1):
        word += text[i]
    return word