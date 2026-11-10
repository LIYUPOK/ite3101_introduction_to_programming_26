n = [3, 5, 7]

for i in range(0, len(n)):
        n[i] = n[i] * 2

def double_list(x: list[int]) -> list[int]:
    for i in range(0, len(x)):
        x[i] = x[i] * 2
# print(double_list(n))
print(double_list(n))
