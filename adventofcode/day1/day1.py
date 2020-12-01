
def main():
    print('Day 1 of the advent code calendar')
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]
    for i in range(0, len(lines)):
        lines[i] = int(lines[i])
    
    # we have to try all combinations to get 2020
    for x in lines:
        for y in lines:
            # print(x, '+', y, ' = ', x+y)
            if x + y == 2020:
                print(x, '+', y, ' = 2020')
                print(x, '*', y, ' = ', x*y)
                exit()
        

if __name__ == '__main__':
    main()