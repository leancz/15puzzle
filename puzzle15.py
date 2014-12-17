from __future__ import print_function
import random

initial = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None ]

def print_puzzle(square):
    for i in range(16):
        if square[i] is None: print('   ', end='')
        else: print("{:3d}".format(square[i]), end='')
        if (i+1) % 4 == 0: print()
             
def move(s, direction):
    # directions can be up, dowm, left or right
    # for the sake of arguments we are moving a tile and not the space
    # so down will swap an upper tile and lower space with each other
    space=s.index(None)
    if ((direction=='d') and (space>3)):
        s[space] = s[space-4]
        s[space-4]=None
    if ((direction=='u') and (space<12)):
        s[space]=s[space+4]
        s[space+4]=None
    if ((direction=='r') and (space not in [0,4,8,12])):
        s[space]=s[space-1]
        s[space-1]=None
    if ((direction=='l') and (space not in [3,7,11,15])):
        s[space]=s[space+1]
        s[space+1]=None

def mix(s):
    # mix up the puzzle - here we do 400 random moves, 25% on
    # average are legal - so around 100 are really done
    moves = ['u', 'd', 'l', 'r']
    for i in range(400):
        move(s, random.choice(moves))



def main():
    cmd=''
    while (cmd not in ['q', 'x', 'stop', 'halt', 'quit']):
        # print square
        print_puzzle(initial)
        # get cmd
        cmd = input('cmd (u, d, l, r, mix, q) : ')
        # process cmd
        if cmd == 'mix': mix(initial)
        else: move(initial, cmd)
        

if __name__ == '__main__':
    main()
