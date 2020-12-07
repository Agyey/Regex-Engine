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
pattern, char = input().strip().split('|')
# Process and Return Output
print(check(pattern, char))
