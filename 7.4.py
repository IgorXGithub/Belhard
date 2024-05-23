def is_merge(s, part1, part2):
    if not s:
        return not part1 and not part2
    if part1 and s[0] == part1[0] and is_merge(s[1:], part1[1:], part2):
        return True
    if part2 and s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]):
        return True
    return False


print(is_merge('kiontrek', 'kio', 'ntrek'))
