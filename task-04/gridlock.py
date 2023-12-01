

n = int(input())
tensor = []

for _ in range(n):
    matrix = []
    for _ in range(3):
        row = input().strip()
        vector = []
        for char in row:
            if not char.isspace():
                vector.append(char)
        matrix.append(vector)
    tensor.append(matrix)

for i in range(n):
    if tensor[i][2][0] == tensor[i][1][1] == tensor[i][0][2]:
        print(tensor[i][1][1])
    elif tensor[i][0][0] == tensor[i][1][1] == tensor[i][2][2]:
        print(tensor[i][1][1])
    elif tensor[i][0][0] == tensor[i][1][0] == tensor[i][2][0]:
        print(tensor[i][1][0])
    elif tensor[i][0][1] == tensor[i][1][1] == tensor[i][2][1]:
        print(tensor[i][1][1])
    elif tensor[i][0][2] == tensor[i][1][2] == tensor[i][2][2]:
        print(tensor[i][1][2])
    elif tensor[i][0][0] == tensor[i][0][1] == tensor[i][0][2]:
        print(tensor[i][0][1])
    elif tensor[i][1][0] == tensor[i][1][1] == tensor[i][1][2]:
        print(tensor[i][1][1])
    elif tensor[i][2][0] == tensor[i][2][1] == tensor[i][2][2]:
        print(tensor[i][2][1])
    else:
        print("DRAW")
