

with open(r'Python\Advent of Code 22\Advent4Input.txt') as r: 
    input = r.read().split('\n')

count = 0
count1 = 0
false = 0
false1 = 0

for pair in input: 
    ids = pair.split(',')
    #print(ids)

    ids1str = ids[0].split('-')
    ids2str = ids[1].split('-')
    ids1 = []
    ids2= []
    for id in ids1str: 
        ids1.append(int(id))
    for id in ids2str: 
        ids2.append(int(id))

    if (ids2[1] >= ids1[1] >= ids2[0] or ids2[1] >= ids1[0] >= ids2[0]): # this is for first inside second
        count += 1
        # print(f'{ids2[0]} <= {ids1[0]} and {ids1[1]} <= {ids2[1]}')
        # print((ids2[0] <= ids1[0] <= ids1[1] <= ids2[1]))
        # print((ids2[0] <= ids1[0] and ids1[1] <= ids2[1]))
    elif(ids1[1] >= ids2[0] >= ids1[0] or ids1[1] >= ids2[1] >= ids1[0]): #this is for second inside first
        count += 1
        # print(f'{ids1[0]} <= {ids2[0]} and {ids2[1]} <= {ids1[1]}')
        # print((ids1[0] <= ids2[0] <= ids2[1] <= ids1[1]))
        # print((ids1[0] <= ids2[0] and ids2[1] <= ids1[1]))
        false1 = 0
    else: 
        false += 0
    
    # if ids1[0] >= ids2[0]: 
    #     print(f'\n {ids1[0]} >= {ids2[0]}')
    #     if ids1[1] <= ids2[1]: 
    #         print(f'{ids2[1]} >= {ids1[1]}')
    #         count += 1
    #         print(f'{ids2[0]} <= {ids1[0]} and {ids1[1]} <= {ids2[1]}')
    # if (ids2[0] <= ids1[0] <= ids1[1] <= ids2[1]): # this is for first inside second
    #     count += 1
    #     print(f'{ids2[0]} <= {ids1[0]} and {ids1[1]} <= {ids2[1]}')
    #     print((ids2[0] <= ids1[0] <= ids1[1] <= ids2[1]))
    #     print((ids2[0] <= ids1[0] and ids1[1] <= ids2[1]))
    # elif(ids1[0] <= ids2[0] and ids2[1] <= ids1[1]): #this is for second inside first
    #     count += 1
    #     print(f'{ids1[0]} <= {ids2[0]} and {ids2[1]} <= {ids1[1]}')
    #     print((ids1[0] <= ids2[0] <= ids2[1] <= ids1[1]))
    #     print((ids1[0] <= ids2[0] and ids2[1] <= ids1[1]))
    #     false1 = 0
    # else: 
    #     false += 0
        #print(False)

# for pair in input: 
#     ids = pair.split(',')
#     #print(ids)

#     ids1 = ids[0].split('-')
#     ids2 = ids[1].split('-')

#     # if ids1[0] >= ids2[0]: 
#     #     print(f'\n {ids1[0]} >= {ids2[0]}')
#     #     if ids1[1] <= ids2[1]: 
#     #         print(f'{ids2[1]} >= {ids1[1]}')
#     #         count += 1
#     #         print(f'{ids2[0]} <= {ids1[0]} and {ids1[1]} <= {ids2[1]}')
#     if ids2[0] <= ids1[0] and ids1[1] >= ids2[1]: 
#         false += 1
#     if ids2[0] >= ids1[0] and ids1[1] >= ids2[1]: 
#         false += 1
#         #print(f'{ids2[0]} <= {ids1[0]} and {ids1[1]} <= {ids2[1]}')
#         #print((ids2[0] <= ids1[0] <= ids1[1] <= ids2[1]))
#     if ids1[0] <= ids2[0] and ids2[1] >= ids1[1]: 
#         count += 1
#         #print(f'{ids1[0]} <= {ids2[0]} and {ids2[1]} <= {ids1[1]}')
#         print((ids1[0] <= ids2[0] <= ids2[1] <= ids1[1]))
#     else: 
#         if(false1 == 1):
#             false += 1 
#         false1 = 0
#         #print(False)

print(count)
#print(count1)
print(false)
#print(false1)