# ==>   Single line comment using # symbol
# ==>   Multi line comment using ''' or """

# stings are enclosed in double quotes without assigned to a variable, Python interpreter automatically ignore it. so we can use it as a comment.
"Hello World"

# Type hinting


# a and b are integers and the return type is also integer, but this is not enforced by the interpreter. we can use any type of data.
def add(a: int, b: int) -> int:
    return a + b


print(add(10, 20))  # 30
