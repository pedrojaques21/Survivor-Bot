from main import *

def A_star(grid, start, end, width, height):
    # Initialize the open and closed lists
    open_list = []
    closed_list = []

    # Add the start cell to the open list
    open_list.append(start)

    # Loop until the open list is empty
    while len(open_list) > 0:
        # Find the cell with the lowest f value
        lowest_f = 50
        lowest_f_index = -1
        for i in range(len(open_list)):
            cell = open_list[i]
            f = cell[2] + cell[3]
            if f < lowest_f:
                lowest_f = f
                lowest_f_index = i

        # Remove the cell with the lowest f value from the open list and add it to the closed list
        current_cell = open_list.pop(lowest_f_index)
        closed_list.append(current_cell)

        # If the current cell is the end cell, return the path
        if current_cell == end:
            path = []
            while current_cell != start:
                path.append(current_cell)
                current_cell = current_cell[4]
            path.append(start)
            path.reverse()
            return path

        # Get the adjacent cells
        adjacent_cells = []
        x = current_cell[0]
        y = current_cell[1]
        if x > 0:
            adjacent_cells.append((x - 1, y))
        if y > 0:
            adjacent_cells.append((x, y - 1))
        if x < width - 1:
            adjacent_cells.append((x + 1, y))
        if y < height - 1:
            adjacent_cells.append((x, y + 1))

        # Loop through the adjacent cells
        for cell in adjacent_cells:
            # If the cell is not traversable or has already been explored, skip it
            if not grid[cell[0]][cell[1]] or cell in closed_list:
                continue

            # If the cell is not in the open list, add it and set its parent
            if cell not in open_list:
                g = current_cell[2] + 1
                h = ((cell[0] - end[0]) ** 2) + ((cell[1] - end[1]) ** 2)
                open_list.append((cell[0], cell[1], g, h, current_cell))


