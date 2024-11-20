def get_matrix(n=3, m=5, value=4):
    i = 0
    j = 0
    list_of_lists = [[i for i in range(n)] for j in range(m)]
    for i in range(0, n):
        for j in range(m):
            list_of_lists[j][i] = value + i + j
    return list_of_lists

print(get_matrix())
print(get_matrix(4,7,1))
