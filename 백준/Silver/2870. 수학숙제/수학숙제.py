import sys
inp=sys.stdin.readline
print(*sorted(sum([[*map(int,''.join((c,' ')[c.isalpha()]for c in inp()).split())]for _ in range(int(inp()))],[])),sep='\n')