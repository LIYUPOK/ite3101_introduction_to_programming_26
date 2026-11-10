n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists: list[list[int]])-> list[int]:
    results = []
    for item in lists:
        for i in item:
            results.append(i)
    return results


print(flatten(n))
