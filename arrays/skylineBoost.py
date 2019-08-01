# In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

# At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

# What is the maximum total sum that the height of the buildings can be increased?

class Solution(object):
  def maxIncreaseKeepingSkyline(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    grid_size = len(grid)
    start = 0
    stop = grid_size
    columns = []
    temp = []
    counter = 0
    
    # rotate array 90deg to get columns
    for i in range(0, grid_size):
      for j in range(0, grid_size):
        columns.append(grid[j][i])

    while stop <= len(columns):
      temp.append(columns[start:stop])
      start += grid_size
      stop += grid_size

    # Max for each column and each row in array format
    max_col = [max(col) for col in temp]
    max_row = [max(row) for row in grid]

    # Increment counter by difference between the current value
    # And the minimum between the row max and the col max
    for i in range(0, grid_size):
      for j in range(0, grid_size):
        target_height = min(max_col[j], max_row[i])
        counter += target_height - grid[i][j]
    
    return counter
        
        
            
        