def main():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]

    validCount = 0

    for line in lines:
        line_split = line.split()
        min_max = line_split[0].split('-')
        pos1 = int(min_max[0])-1
        pos2 = int(min_max[1])-1
        char = line_split[1].strip(':')
        passwd = line_split[2]

        valid_passwd = False
        if passwd[pos1] == char:
            valid_passwd = not valid_passwd
        if passwd[pos2] == char:
            valid_passwd = not valid_passwd

        if valid_passwd:
            print(char,'can be found at position', pos1, 'or', pos2, 'of', passwd, 'but not at both')
            validCount += 1

    print(validCount)


if __name__ == '__main__':
    main()