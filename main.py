def main():
    while True:
        try:
            x = int(input("Enter a number greater than 0: "))
            if(x>0):
                break
            else:
                print("Enter a number greater than 0")
        except ValueError:
            print("Please enter a number")

    total = 0
    for i in range(x):
        while True:
            try:
                number = float(input(f"Enter a value for item {1+i}: "))
                total += number
                break
            except ValueError:
                print("Enter a number")
    
    average = total/x
    print(f'the average is {average:.2f}')

if __name__ == '__main__':
    main()
