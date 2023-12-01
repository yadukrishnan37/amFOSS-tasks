

def hello(s):
    h = "hello"
    i = 0

    for char in s:
        if char == h[i]:
            i += 1
            if i == len(h):
                return 1

    return 0

if hello(input()):
    print('YES')
else:
    print('NO')
