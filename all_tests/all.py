import re
def printValue():
    while True:
        try:
            x = int(input('enter an number greater than 0'))
            if(x>0):
                break
            print('number greater than 0')
        except ValueError:
            print('enter a number')
    print(x)

def rearrange(name):
    result = re.search(r'^([\w.]*), ([\w.]*)$',name)
    return f'{result[2]}, {result[1]}'
