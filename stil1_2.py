list_data = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i=0
while i < len(list_data):
    if list_data[i] > 0:
        print(list_data[i])
    else:
        continue
    i += 1
