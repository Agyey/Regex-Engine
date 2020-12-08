def single_char_match(re, char):
    return re == '' or char == re or (re == '.' and char != '')

def equal_length_match(re, string):
    if re == '':
        return True
    if string == '':
        return False
    if not single_char_match(re[0], string[0]):
        return False
    return equal_length_match(re[1:], string[1:])

def match(re, string):
    return equal_length_match(re, string)

print(match(*input().split('|')))
