def valid_password(p):
    prev = -1
    consecutive_digits = 0
    # has_adjacent_same_digits = False
    has_two_consecutive_digits = False
    for c in map(int, p):
        if c < prev: return False
        if c == prev:
            consecutive_digits += 1
        else:
            if consecutive_digits == 2:
                has_two_consecutive_digits = True
            consecutive_digits = 1
        prev = c
    if consecutive_digits == 2:
        has_two_consecutive_digits = True
    return has_two_consecutive_digits

# print(valid_password('111111'))
# print(valid_password('223450'))
# print(valid_password('123789'))

# print(valid_password('112233'))
# print(valid_password('123444'))
# print(valid_password('111122'))

print(len([p for p in range(145852, 616942+1) if valid_password(str(p))]))
