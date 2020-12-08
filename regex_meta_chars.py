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
        return True
    elif pattern.startswith('^') and pattern.endswith('$'):
        if match_len == (len(input_string) + 2):
            return match(pattern[1:-1], input_string[:match_len-2])
        else:
            return False
    elif pattern.startswith('^'):
        return match(pattern[1:], input_string[:match_len-1])
    elif pattern.endswith('$'):
        return match(pattern[:-1], input_string[-(match_len-1):])
    elif match_len and match_len <= len(input_string):
        for i in range(0, len(input_string)-match_len+1):
            if match(pattern, input_string[i:i+match_len]):
                return True
    return False

# Take Input
pattern, input_string = input().strip().split('|')
# Process and Return Output
print(full_match(pattern, input_string))
