def main():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]

    validCount = 0

    for line in lines:
        line_split = line.split()
        min_max = line_split[0].split('-')
        char = line_split[1].strip(':')
        passwd = line_split[2]

        charCount = passwd.count(char)
        if charCount >= int(min_max[0]) and charCount <= int(min_max[1]):
            validCount += 1

    print(validCount)

if __name__ == '__main__':
    main()