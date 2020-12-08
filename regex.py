def single_char_match(re, char, escape=False):
    return re == '' or char == re or ((not escape and re == '.') and char != '')

def equal_length_match(re, string, escape=False):
    if re == '' or (re == '$' and string == ''):
        return True
    if string == '':
        return False
    if re[0] == '\\':
        escape = True
        re = re[1:]
    if len(re) > 1 and re[1] in '*?+':
        if re[1] in '?*' and equal_length_match(re[2:], string, escape):
            return True
        if single_char_match(re[0], string[0], escape) and (
                (re[1] in '?+' and equal_length_match(re[2:], string[1:], escape)) or
                (re[1] in '*+' and equal_length_match(re, string[1:], escape))):
            return True

    if not single_char_match(re[0], string[0], escape):
        return False
    return equal_length_match(re[1:], string[1:], escape)

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
