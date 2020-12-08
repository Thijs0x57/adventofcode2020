def main():
    print('Day x of the advent code calendar')
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]
    row = 0
    fb_max = 128
    fb_min = 0
    lr_max = 8
    lr_min = 0
    for line in lines:
        front_back, left_right = [], []
        front_back[:0], left_right[:0] = line[:7], line[7:]
        print(front_back, left_right)
        print('min_max:', fb_min, fb_max)

        row = determine_in_range(front_back, fb_min, fb_max, "B", "F")-1
        for fb in front_back:
            if fb == "F":
                fb_max -= int((fb_max-fb_min) / 2)
                if fb_max - fb_min == 1:
                    row = fb_min
            if fb == "B":
                fb_min += int((fb_max-fb_min) /2)
                if fb_max - fb_min == 1:
                    row = fb_max
            print('fb:', fb, fb_min, fb_max)
            
        row -= 1
        fb_max = 128
        fb_min = 0

def determine_in_range(range, min, max, up_char, down_char):
    _min = min
    _max = max
    print('min max:', _min, _max)
    for r in range:
        if r == down_char:
            _max -= int((_max-_min) / 2)
            if _max - _min == 1:
                return _min
        if r == up_char:
            _min += int((_max-_min) /2)
            if _max - _min == 1:
                return _max
        print('r:', r, _min, _max)
    _min = min
    _max = max

if __name__ == '__main__':
    main()