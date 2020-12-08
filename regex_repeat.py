import sys
sys.setrecursionlimit(10000)


# Matches two chars
def check(pattern, char):
    if char:
        if pattern in ['', '.']:
            return True
        elif pattern == char:
            return True
        else:
            return False
    else:
        if pattern:
            return False
        else:
            return True


# Matches two equal length strings
def match(pattern, input_string):
    return len(pattern) == 0 or (len(pattern) == len(input_string) and all([check(p, c)for p, c in zip(pattern, input_string)]))


# Matches all substrings of input_string
def full_match(pattern, input_string):
    match_len = len(pattern)
    if not match_len:
        return True, None
    elif '?' in pattern or '+' in pattern or '*' in pattern:
        if '?' in pattern:
            i = pattern.index('?')
            pre_pattern = pattern[:i-1]
            post_pattern = "^"+pattern[i+1:]
            repeat_char = pattern[i-1]
            if len(pre_pattern):
                c, s = full_match(pre_pattern, input_string)
            else:
                c, s = True, 0
            if c and s+len(pre_pattern) < len(input_string):
                if repeat_char == '.':
                    repeat_char = input_string[s+len(pre_pattern)]
                if check(repeat_char, input_string[s+len(pre_pattern)]):
                    return full_match(post_pattern, input_string[s+len(pre_pattern) + 1:])[0], s
                else:
                    return full_match(post_pattern, input_string[s+len(pre_pattern):])[0], s
            else:
                return False, None
        elif '*' in pattern:
            i = pattern.index('*')
            pre_pattern = pattern[:i-1]
            post_pattern = "^"+pattern[i+1:]
            repeat_char = pattern[i-1]
            if len(pre_pattern):
                c, s = full_match(pre_pattern, input_string)
            else:
                c, s = True, 0
            if c and s+len(pre_pattern) < len(input_string):
                if repeat_char == '.':
                    repeat_char = input_string[s+len(pre_pattern)]
                if check(repeat_char,input_string[s+len(pre_pattern)]):
                    offset = 0
                    while(s+len(pre_pattern)+offset+1 < len(input_string)):
                        offset += 1
                        if not check(repeat_char,input_string[s+len(pre_pattern)+offset]):
                            break
                    return full_match(post_pattern, input_string[s+len(pre_pattern) + offset:])[0], s
                else:
                    return full_match(post_pattern, input_string[s+len(pre_pattern):])[0], s
            else:
                return False, None
        elif '+' in pattern:
            i = pattern.index('+')
            pre_pattern = pattern[:i-1]
            post_pattern = "^"+pattern[i+1:]
            repeat_char = pattern[i-1]
            if len(pre_pattern):
                c, s = full_match(pre_pattern, input_string)
            else:
                c, s = True, 0
            if c and s+len(pre_pattern) < len(input_string):
                if repeat_char == '.':
                    repeat_char = input_string[s+len(pre_pattern)]
                if check(repeat_char,input_string[s+len(pre_pattern)]):
                    offset = 0
                    while(s+len(pre_pattern)+offset+1 < len(input_string)):
                        offset += 1
                        if not check(repeat_char,input_string[s+len(pre_pattern)+offset]):
                            break
                    return full_match(post_pattern, input_string[s+len(pre_pattern) + offset:])[0], s
                else:
                    return False, None
            else:
                return False, None
    elif pattern.startswith('^') and pattern.endswith('$'):
        if match_len == (len(input_string) + 2):
            return match(pattern[1:-1], input_string[:match_len - 2]), 0
        else:
            return False, None
    elif pattern.startswith('^'):
        return match(pattern[1:], input_string[:match_len - 1]), 0
    elif pattern.endswith('$'):
        return match(pattern[:-1], input_string[-(match_len - 1):]), -(match_len - 1)
    elif match_len and match_len <= len(input_string):
        for i in range(0, len(input_string)-match_len+1):
            if match(pattern, input_string[i:i+match_len]):
                return True, i
    return False, None

# Take Input
pattern, input_string = input().strip().split('|')
# Process and Return Output
print(full_match(pattern, input_string)[0])
