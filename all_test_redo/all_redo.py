import re

def main():
    while True:
        try:
            x = int(input("Enter an integer greater than 0: "))
            if(x>0):
                break
            print("The integer should be greater than 0")
        except ValueError:
            print('Doesnt accept non-integer values')
    
    total = 0
    for i in range(x):
        while True:
            try:
                n = int(input(f"enter the {i+1} value: "))
                total += n
                break
            except ValueError:
                print('Doesnt accept non-integer values')
    average = total / x
    print(f'your average is {average}')

def rearrange_name(name):
    result = re.search(r'^([\w.]*), ([\w.]*)$', name)
    if result is None:
        return name
    return f'{result[2]}, {result[1]}'