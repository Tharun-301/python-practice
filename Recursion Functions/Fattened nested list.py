def flatten(L):
    for e in L:
        if hasattr(e, '__iter__'):
            yield from flatten(e)
        else:
            yield e


L = flatten([1,2,[3,[4,5],6,7],8])

flat = flatten(L)

flat_list = list(flat)
print(flat_list)