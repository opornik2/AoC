from math import sqrt, prod
import sys

with open(sys.argv[1], mode="r", encoding="utf-8") as f:
    node_coords = [
        tuple(map(int, row.split(",")))
        for row in f.read().strip().splitlines()
    ]


node_pairs_by_dist = {
    sqrt(sum((m[k] - n[k]) ** 2 for k in (0, 1, 2))): (i, j)
    for i, n in enumerate(node_coords)
    for j, m in enumerate(node_coords[i + 1 :], i + 1)
}
sorted_dists = sorted(node_pairs_by_dist.keys())
circuits = [{i} for i in range(len(node_coords))]
circuit_indices_by_node = {i: i for i in range(len(node_coords))}
circuit_count = len(circuits)


for connection_count, dist in enumerate(sorted_dists):
    node_i, node_j = node_pairs_by_dist[dist]
    print(f"{node_i} - {node_j}")
    ci = circuit_indices_by_node[node_i]
    cj = circuit_indices_by_node[node_j]
    if ci != cj:
        circuits[ci].update(circuits[cj])
        for node in circuits[cj]:
            circuit_indices_by_node[node] = ci
        circuits[cj] = {}
        circuit_count -= 1
    connection_count += 1
    print(f"conn_count={connection_count}\tdist={dist}\n")
    if connection_count == int(sys.argv[2]):
        part_1 = prod(sorted([len(c) for c in circuits if c])[-3:])
        break
    if circuit_count == 1:
        break


part_2 = node_coords[node_i][0] * node_coords[node_j][0]



print(f"Part 1: {part_1}")
#\nPart 2: {part_2}")
