import numpy as np


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)




def process_grids(grids):
    if not grids:
        return []

    L = grids[0].shape[0]  # Assuming all grids are square and of the same size
    results = []
    uf = UnionFind(L*L)

    # Helper function to perform union operations for a newly occupied site
    def update_union_find(grid, i, j):
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Check four adjacent sites
            ni, nj = i + di, j + dj
            if 0 <= ni < L and 0 <= nj < L and grid[ni][nj] == 1:
                uf.union(i * L + j, ni * L + nj)

    # Process first grid from scratch
    for i in range(L):
        for j in range(L):
            if grids[0][i][j] == 1:
                update_union_find(grids[0], i, j)
    results.append(check_percolation(uf, L))  # Assuming check_percolation is a function that checks for percolation

    # Process subsequent grids based on the change from the previous grid
    for grid_index in range(1, len(grids)):
        previous_grid, current_grid = grids[grid_index - 1], grids[grid_index]
        diff = np.where(current_grid != previous_grid)
        for i, j in zip(diff[0], diff[1]):
            if current_grid[i][j] == 1:  # Only interested in newly occupied sites
                update_union_find(current_grid, i, j)
        results.append(check_percolation(uf, L))

    return results

# Assuming existence of a check_percolation function
def check_percolation(uf, L):
    for j in range(L):
        for k in range(L):
            if uf.connected(0 * L + j, (L-1) * L + k):
                return 1
    return 0