from collections import Counter

with open(r'Python\Advent of Code 22\Advent3Input.txt') as r: 
    input = r.read().split('\n')
#print(input)

cumpriority = 0

# for item in input: 
# # item = input[0]
# # if 1 ==1: 
#     length = len(item)
#     #print(item)
#     #print(type(item))
#     #print(length)
#     #print(int(length/2-1))
#     comp1 = item[:int(length/2)]
#     comp2 = item[int(length/2):]
#     #print(f'{comp1} and {comp2}')
#     dict1 = Counter(comp1)
#     dict2 = Counter(comp2)
#     #print(dict1)
#     for key in dict1: 
#         if key in dict2: 
#             mistake = key
#             print(key)
#     if mistake.islower(): 
#         cumpriority += ord(mistake) - 96
#         print(cumpriority)
#     else: 
#         cumpriority += ord(mistake) - 38
#         print(cumpriority)
person0 = []
person1 = []
person2 = []

for item in input:
    tempDict = Counter(item) 
    if (input.index(item) % 3 == 0):
        person0.append(tempDict)
    if (input.index(item) % 3 == 1):
        person1.append(tempDict)
    if (input.index(item) % 3 == 2):
        person2.append(tempDict)
    
    
if(1==1):
    for bag in person0: 
        print(bag)
        for key in bag: 
            if key in person1[person0.index(bag)] and key in person2[person0.index(bag)]:
                badge = key
                print(badge)
        if badge.islower():
            cumpriority += ord(badge) - 96
            print(cumpriority)
        else: 
            cumpriority += ord(badge) - 38
            print(cumpriority)


print(cumpriority)