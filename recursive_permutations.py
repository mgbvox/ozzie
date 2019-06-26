def permutations(v, is_top = True):
    if len(v) == 0 or len(v) == 1:
        return [v]
    p_list = []
    for idx,l in enumerate(v):
        rest = [j for i,j in enumerate(v) if i != idx]
        perms = permutations(rest, is_top=False)
        for perm in perms:
            p_list.append([l]+perm)
    return p_list

print([''.join(i) for i in permutations('test')])