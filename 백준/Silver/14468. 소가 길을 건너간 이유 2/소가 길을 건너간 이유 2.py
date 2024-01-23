a={chr(65+i)for i in range(26)}
b=set()
d={c:set()for c in a}
for c in input():
    if c in a:
        for k in b:
            d[k].add(c)
        a.discard(c)
        b.add(c)
    elif c in b:
        for k in b-{c}:
            d[k].discard(c)
        b.discard(c)
print(sum(len(v)for v in d.values()))