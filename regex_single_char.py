def single_char_match(re, char):
    return re == '' or char == re or (re == '.' and char != '')

def match(re, char):
    if re == '':
        return True
    return single_char_match(re, char)

print(match(*input().split('|')))
