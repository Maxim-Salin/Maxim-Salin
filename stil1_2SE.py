list_data = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i=0
stop = False
n = 1
while i < len(list_data) and n >= 0 :
    if list_data[i] > 0:
        print(list_data[i])
    # elif list_data[i] == 0:
    #      stop = True
    else:
        n = int(list_data[i])
        i += 1
        continue
    i += 1

