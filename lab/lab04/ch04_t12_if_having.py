def using_control_once() -> str:
    if "HELLO" == "HELLO" and 1 + 1 == 3 - 1:
        return "Success #1"


def using_control_again() -> str:
    if False or True:
        return "Success #2"


print(using_control_once())
print(using_control_again())
