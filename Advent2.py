import os 
print(os.listdir())
print(os.getcwd())

with open(r'Python\Advent of Code 22\Advent2Input.txt') as r: 
    input = r.read().split('\n')

points = 0

def partOne():
    for game in input:
        if(game[0] == 'A'): #op plays rock
            if(game[2] == 'X'): 
                points += 3 + 1
            if(game[2] == 'Y'): 
                points += 6 + 2 
            if(game[2] == 'Z'): 
                points += 0 + 3
        
        if(game[0] == 'B'): # op plays paper
            if(game[2] == 'X'): 
                points += 0 + 1
            if(game[2] == 'Y'): 
                points += 3 + 2 
            if(game[2] == 'Z'): 
                points += 6 + 3
        
        if(game[0] == 'C'): #op plays scizzors
            if(game[2] == 'X'): 
                points += 6 + 1
            if(game[2] == 'Y'): 
                points += 0 + 2 
            if(game[2] == 'Z'): 
                points += 3 + 3

print(points)

if(1==1):
    for game in input:
        if(game[0] == 'A'): #op plays rock
            if(game[2] == 'X'): 
                points += 0 + 3
            if(game[2] == 'Y'): 
                points += 3 + 1
            if(game[2] == 'Z'): 
                points += 6 + 2
        
        if(game[0] == 'B'): # op plays paper
            if(game[2] == 'X'): 
                points += 0 + 1
            if(game[2] == 'Y'): 
                points += 3 + 2
            if(game[2] == 'Z'): 
                points += 6 + 3
        
        if(game[0] == 'C'): #op plays scizzors
            if(game[2] == 'X'):
                points += 0 + 2
            if(game[2] == 'Y'): 
                points += 3 + 3
            if(game[2] == 'Z'): 
                points += 6 + 1

print(points)

#print(input)
