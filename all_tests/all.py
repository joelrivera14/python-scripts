import re
def main():
    while True:
        try:
            x = int(input("Enter a number greater than zero"))
            if(x>0):
                break
            print('must be greater than zero')
        except ValueError:
            print('must be a number')
    
    print(x)

def rearrange(name):
    result = re.search(r'^([\w.]*), ([\w.]*)$', name)
    if result is None:
        return name
    return f'{result[2]}, {result[1]}'



        
