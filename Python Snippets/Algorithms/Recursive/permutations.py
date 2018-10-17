#
# Generate All Permutations of a Sequence
#
# Joel Rorseth
#



# Permutations (unordered)
def permutations(seq):
    perms = []
    _permute(seq, 0, perms)
    return perms

def _permute(seq, ptr, perms):

    if ptr == len(seq):
        perms.append(seq[:])
        return

    for i in range(ptr, len(seq)):

        seq[ptr], seq[i] = seq[i], seq[ptr]
        _permute(seq, ptr+1, perms)
        seq[ptr], seq[i] = seq[i], seq[ptr]




# Permutations in sorted order
def permutations_sorted(seq):
    perms = []
    _permute_sorted(seq, [], perms)
    return perms

def _permute_sorted(seq, path, perms):

    if len(path) == len(seq):
        perms.append(path[:])
    else:
        for element in seq:
            if element not in path:
                path.append(element)
                _permute_sorted(seq, path, perms)
                path.remove(element)





print("\n".join(str(p) for p in permutations([1,2,3,4])))
