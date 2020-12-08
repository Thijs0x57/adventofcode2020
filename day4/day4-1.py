import re

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

    # validate_hcl("#888785")
        
def check_passports(passports):
    valid_count = 0
    for p in passports:
        if "byr" in p and "iyr" in p and "eyr" in p and "hgt" in p and "hcl" in p and "ecl" in p and "pid" in p:
            # print('passport:',p)
            if check_passport(p) == True:
                print('passport is valid!!!')
                valid_count += 1
    
    print('amount valid passports:',valid_count)

def check_passport(passport):
    byr = int(passport.get("byr"))
    iyr = int(passport.get("iyr"))
    eyr = int(passport.get("eyr"))
    hgt = passport.get("hgt")
    hcl = passport.get("hcl")
    ecl = passport.get("ecl")
    pid = passport.get("pid")
    # print(passport)
    if byr >= 1920 and byr <= 2002:
        # print('byr',byr, 'is valid')
        if iyr >= 2010 and iyr <= 2020:
            # print('iyr',iyr, 'is valid')
            if eyr >= 2020 and eyr <= 2030:
                # print('eyr',eyr, 'is valid')
                if validate_hgt(hgt) == True and validate_hcl(hcl) == True and validate_ecl(ecl) == True and validate_pid(pid) == True:
                    print('passport:',passport,'is valid')
                    return True
    
    return False

def validate_hgt(hgt):

    l, r = int(hgt[:-2]), hgt[-2:]
    if r == "cm" and l >= 150 and l <= 193:
        return True
    if r == "in" and l >= 59 and l <= 76:
        return True
    return False

def validate_hcl(hcl):
    if bool(re.search("^#([0-9a-f]{6})$", hcl)):
        # print('hcl:',hcl, "matches the regex")
        return True
    return False

def validate_ecl(ecl):
    if ecl == "amb" or ecl == "blu" or ecl == "brn" or ecl == "gry" or ecl == "grn" or ecl == "hzl" or ecl == "oth":
        # print('ecl:',ecl,'is valid')
        return True
    return False

def validate_pid(pid):
    print('checking pid:',pid)
    if bool(re.search("^[0-9]{9}$", str(pid))):
        print('pid:',pid, 'matches the regex')
        return True
    return False

def parse_passport(passport_items):
    pass_items = passport_items.split(" ")
    _passport = {}
    for item in pass_items:
        item_key_value = item.split(":")
        _passport[item_key_value[0]] = item_key_value[1]

    return _passport


if __name__ == '__main__':
    main()