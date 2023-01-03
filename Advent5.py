def checkSpace(space): 
    if(space == ' '): 
        return False 
    return True

col1 = [] 
col2 = []
col3 = [] 
col4 = []
col5 = [] 
col6 = []
col7 = [] 
col8 = []
col9 = []

with open(r'Python\Advent of Code 22\Advent5Input.txt') as r: 
    input = r.read().split('\n')

    # The start of the array is the top of the stack 

    for i in range(8): 
        line = input[0]
        print(i)
        print(line)
        if (checkSpace(line[1])):
            col1.append(line[1])
        if (checkSpace(line[5])):
            col2.append(line[5])
        if (checkSpace(line[9])):
            col3.append(line[9])
        if (checkSpace(line[13])):
            col4.append(line[13])
        if (checkSpace(line[17])):
            col5.append(line[17])
        if (checkSpace(line[21])):
            col6.append(line[21])
        if (checkSpace(line[25])):
            col7.append(line[25])
        if (checkSpace(line[29])):
            col8.append(line[29])
        if (checkSpace(line[33])):
            col9.append(line[33])
        input.pop(0)
input.pop(0)
input.pop(0)

for direction in input: 
    order = direction.split(' ')
    number = int(order[1])
    fromCol = int(order[3])
    toCol = int(order[5])
    print(f'From: {fromCol} Number: {number} To: {toCol}')

    for n in reversed(range(number)): 
        exec(f'col{toCol}.insert(0, col{fromCol}[{n}])')
        exec(f'col{fromCol}.pop({n})')

print(f'{col1[0]}{col2[0]}{col3[0]}{col4[0]}{col5[0]}{col6[0]}{col7[0]}{col8[0]}{col9[0]}')