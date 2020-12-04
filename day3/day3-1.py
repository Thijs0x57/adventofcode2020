def main():
    print('Day 3 of the advent code calendar')
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]

        
    line_len = len(lines[0])
    # navigate the map, which repeats to the right infinitely
    # start at top left
    # move: right x, down y
    # count number of trees that would be encountered
    path0 = check_slope_path(lines, 1, 1, line_len)
    path1 = check_slope_path(lines, 3, 1, line_len)
    path2 = check_slope_path(lines, 5, 1, line_len)
    path3 = check_slope_path(lines, 7, 1, line_len)
    path4 = check_slope_path(lines, 1, 2, line_len)

    print('answer:', path0*path1*path2*path3*path4)
    

def check_slope_path(lines, right, down, line_len):
    OPEN_SQUARE = '.'
    TREE = '#'
    tree_count = 0
    x_pos = 0
    line_count = 0
    for line in lines:
        # print('line count:',line_count,'down:',down,'modulo:', line_count % down)
        if line_count % down > 0:
            line_count += 1
            continue

        slope = list(line)
        rel_pos = x_pos % line_len

        if slope[rel_pos] == OPEN_SQUARE:
            # not a tree
            slope[rel_pos] = 'O'
        elif slope[rel_pos] == TREE:
            # a tree
            tree_count += 1
            slope[rel_pos] = 'X'

        x_pos += right
        line_count += 1
        # print(''.join(slope))

    print('trees encountered:', tree_count)
    return tree_count

if __name__ == '__main__':
    main()