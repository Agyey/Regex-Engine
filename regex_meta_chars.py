def single_char_match(re, char):
    return re == '' or char == re or (re == '.' and char != '')

def equal_length_match(re, string):
    if re == '' or (re == '$' and string == ''):
        return True
    if string == '':
        return False
    if not single_char_match(re[0], string[0]):
        return False
    return equal_length_match(re[1:], string[1:])

def match(re, string):
    if re == '':
        return True
    if re[0] == '^':
        return equal_length_match(re[1:], string)
    for i in range(len(string)):
        if equal_length_match(re, string[i:]):
            return True
    return False

print(match(*input().split('|')))
