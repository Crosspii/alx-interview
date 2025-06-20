#!/usr/bin/python3
"""Module to calculate the perimeter of an island represented in a grid."""


def island_perimeter(grid):
    """Calculate the perimeter of an island in a grid.

    Args:
        grid (list of list of int): 2D grid representing
        the island (1 for land, 0 for water).

    Returns:
        int: The perimeter of the island.
    """
    visited = set()

    def dfs(x, y):
        """Depth-first search to explore the island."""
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0])\
                or grid[x][y] == 0:
            return 1  # Count water or out of bounds as perimeter
        if (x, y) in visited:
            return 0
        visited.add((x, y))
        perim = dfs(x + 1, y)  # Down
        perim += dfs(x - 1, y)        # Up
        perim += dfs(x, y + 1)  # Right
        perim += dfs(x, y - 1)
        return perim

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                return dfs(x, y)
    return 0  # If no land is found, perimeter is 0
