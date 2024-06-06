# Input : grid[][] = {{1, 0, 0, 0, 1},
#                    {0, 0, 0, 0, 0},
#                    {0, 0, 1, 0, 0}};
# Output : 6
# Best meeting point is (0, 2).
# Total distance traveled is 2 + 2 + 2 = 6

grid = [[1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]]

rows = len(grid)
cols = len(grid[0])

x_coor = []
y_coor = []

for  r in range(rows):
    for c in range(cols):
        if grid[r][c] == 1:
            x_coor.append(r)
            y_coor.append(c)
print(x_coor)
print(y_coor)

x_coor.sort()
y_coor.sort()
# finding the median of two list
median_x_coor = x_coor[len(x_coor)//2]
median_y_coor = y_coor[len(y_coor)//2]

# calculating sum because median minimizes the sum of absolute deviations

total_dist = 0
for x in x_coor:
    total_dist += abs(x-median_x_coor)
for y in y_coor:
    total_dist += abs(y-median_y_coor)
print(total_dist)
