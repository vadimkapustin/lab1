import time, math

RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m' # сброс
ERASE = '\x1B[2K' # erase the line
BEGIN = '\x1B[1G' # return to column 1



def flag():
    line = ' ' * 10
    lenght = 10
    height = lenght

    for i in range(lenght):
            print(f'{BLUE}{line}{WHITE}{line}{RED}{line}{END}')



def chess_board():
    lenght = 15
    height = 6
    line = ' ' * 5
    for i in range(1, height+1):
        if i <= 2:
            print(f'{WHITE}{line}{END}     {WHITE}{line}{END}')
        elif 2 < i <= 4:
            print(f'     {WHITE}{line}{END}     ')
        else:
            print(f'{WHITE}{line}{END}     {WHITE}{line}{END}')

def function():
    Oy = 9
    Ox = 3
    for y in range(Oy, -1, -1):
        if y == 0:
            line = '#'
        elif int((y**0.5) % 1 * 100) == 0:
            line = '     ' * (int(y**0.5)-1) + ' '*4 + '#'
        elif int((y**0.5) % 1 * 100) >= 75:
            line = '     ' * (math.ceil(y**0.5)-1) + ' '*4 + '#'
        elif 50 <= int((y**0.5) % 1 * 100) < 75:
            line = '     ' * (math.ceil(y**0.5)-1) + ' '*3 + '#'
        elif 25 <= int((y**0.5) % 1 * 100) < 50:
            line = '     ' * (math.ceil(y**0.5)-1)+ ' '*2 + '#'
        elif 0 < int((y**0.5) % 1 * 100) < 25:
            line = '     ' * (math.ceil(y**0.5)-1) + '#'
        print(f'{y}{line}')
    print('0    1    2    3')

def seq():
    a = []
    otr = []
    pol = []
    f = open('lab1\\sequence.txt')
    for x in f:
        a.append(float(x))
    for n in a:
        if n > 0:
            pol.append(n)
        if n < 0:
            otr.append(n)
    proc_pol = len(pol)/len(a) * 100
    proc_otr = len(otr)/len(a) * 100
    bar = 50
    pol_bar = int(proc_pol / 100 * bar)
    otr_bar = int(proc_otr / 100 * bar)
    line = ' '
    print(f"Положительные: {BLUE}{proc_pol}%  {line * pol_bar} {END}")
    print(f"Отрицательные: {RED}{proc_otr}%  {line * otr_bar} {END}")


            
    
#flag()
#chess_board()
#function()
#seq()

