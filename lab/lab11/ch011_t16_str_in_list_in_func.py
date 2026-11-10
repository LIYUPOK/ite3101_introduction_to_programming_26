n = ["Michael", "Lieberman"]
# Add your function here
def join_string(words):
    result = ""
    for i in words:
        result += i + ""
    return result

print(join_string(n))
