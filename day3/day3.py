def main():
    print('Day 3 of the advent code calendar')
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]

        OPEN_SQUARE = '.'
        TREE = '#'

    # navigate the map, which repeats to the right infinitely
    # start at top left
    # move: right 3, down 1
    # count number of trees that would be encountered

    tree_count = 0
    x_pos = 0
    line_len = len(lines[0])
    for line in lines:
        slope = list(line)
        rel_pos = x_pos % line_len

        if slope[rel_pos] == OPEN_SQUARE:
            # not a tree
            slope[rel_pos] = 'O'
        elif slope[rel_pos] == TREE:
            # a tree
            tree_count += 1
            slope[rel_pos] = 'X'

        x_pos += 3
        print(''.join(slope))

    print('trees encountered:', tree_count)

if __name__ == '__main__':
    main()