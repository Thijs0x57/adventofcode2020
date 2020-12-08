def main():
    print('Day 4 of the advent code calendar')
    with open('input.txt') as f:
        lines = [line for line in f]

    passports = []
    passport_line=""
    for line in lines:
        # print('line:',repr(line))
        if line == "\n":
            passports.append(parse_passport(passport_line[:-1]))
            passport_line=""
            continue
        passport_line += line.replace("\n", " ")
        
    check_passports(passports)
        
def check_passports(passports):
    valid_count = 0
    for p in passports:
        if "byr" in p and "iyr" in p and "eyr" in p and "hgt" in p and "hcl" in p and "ecl" in p and "pid" in p:
            valid_count += 1
    
    print('amount valid passports:',valid_count)


def parse_passport(passport_items):
    pass_items = passport_items.split(" ")
    _passport = {}
    for item in pass_items:
        item_key_value = item.split(":")
        _passport[item_key_value[0]] = item_key_value[1]

    return _passport


if __name__ == '__main__':
    main()