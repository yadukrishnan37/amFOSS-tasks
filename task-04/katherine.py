

t = int(input())

for _ in range(t):
    n = int(input())
    column = []  
    matrix = []
    sequence = []
    for _ in range(n):
        vector = list(map(int, input('').split()))
        column.append(vector[-1]) 
        matrix.append(vector)

    least = min(column, key=column.count)
    most = max(set(column), key=column.count)
    i = column.index(least)
    
    sequence = matrix[i].copy()
    sequence.append(most)

    print(' '.join(map(str, sequence)))


