import sys
import re
from collections import defaultdict


def part1(puzzle_input):
    graph = defaultdict(set)
    for a, b in re.findall(r'(\w+)-(\w+)', puzzle_input):
        graph[a].add(b)
        graph[b].add(a)

    candidates = [c for c in graph if c.startswith('t')]
    t_triples = set()
    for t in candidates:
        for a in graph[t]:
            for b in graph[a]:
                if b in graph[t]:
                    t_triples.add(tuple(sorted([t, a, b])))

    return len(t_triples)

def part2(puzzle_input):
    graph = defaultdict(set)
    for a, b in re.findall(r'(\w+)-(\w+)', puzzle_input):
        graph[a].add(b)
        graph[b].add(a)

    def bron_kerbosch(selected, candidates, excluded):
        if not candidates and not excluded:
            return selected
        
        max_clique = set()
        for v in candidates.copy():
            clique = bron_kerbosch(
                selected.union({v}), 
                candidates.intersection(graph[v]), 
                excluded.intersection(graph[v])
            )
            max_clique = max(max_clique, clique, key=len)
            candidates.remove(v)
            excluded.add(v)

        return max_clique

    max_clique = bron_kerbosch(set(), set(graph), set())
    return ','.join(sorted(max_clique))

with open(sys.argv[1], "r") as FH:
    inp = FH.read().strip()
print(part1(inp))
print(part2(inp))

