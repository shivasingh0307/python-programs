row_num = int(input("Enter row number: "))
col_num = int(input("Enter column number: "))

multi_list = [[0 for col in range (col_num)]for row in range (row_num)]


for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col] = row*col

    print(multi_list)    