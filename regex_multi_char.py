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

# Take Input
pattern, str = input().strip().split('|')
# Process and Return Output
print(len(pattern) == 0 or (len(pattern) == len(str) and all([check(p, c)for p, c in zip(pattern, str)])))
