def neighbours(row, col, l):
    cnt = 0
    for x in range(row-1, row+2):
        if(x < 0 or x > len(l)-1):
            continue
        else:
            for y in range(col-1, col+2):
                if(x == row and y == col):
                    continue
                if(y < 0 or y > len(l[x])-1):
                    continue
                else:
                    cnt += int(l[x][y])
    return cnt
def game(l):
    lNew = []
    for x in range(len(l)):
        a = []
        for y in range(len(l[x])):
            a.append(l[x][y])
        lNew.append(a)
    for row in range(len(l)):
        for col in range(len(l[row])):
            if(l[row][col] == '0'):
                if(neighbours(row, col, l) == 3):
                    lNew[row][col] = '1'
            else:
                if(neighbours(row, col, l) not in (2, 3)):
                    lNew[row][col] = '0'
    return lNew