row = 9
col = 9
matrix = []

for _ in range(row):
    matrix.append(list(map(int, input().split())))

max_val = matrix[0][0]
max_i, max_j = 1,1    # 1-based로 저장

for i in range(row):
    for j in range(col):
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            max_i = i + 1
            max_j = j + 1

print(max_val)
print(max_i, max_j)
