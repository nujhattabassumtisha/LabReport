import random
def generate_grid(N):
 return [['O' if random.random() > 0.2 else '1' for _ in 
range(N)] for _ in range(N)]
def get_valid_position(grid, N):
 while True:
 x, y = random.randint(0, N-1), random.randint(0, N-1)
 if grid[x][y] == 'O':
 return (x, y)
def dfs(grid, start, goal, N):
 stack, visited, parent = [start], set(), {}
 order = []
 
 while stack:
 x, y = stack.pop()
 if (x, y) in visited:
 continue
 
 visited.add((x, y))
 order.append((x, y))
 
 if (x, y) == goal:
 break
 
 for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
 nx, ny = x + dx, y + dy
 if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 'O' and 
(nx, ny) not in visited:
 stack.append((nx, ny))
 parent[(nx, ny)] = (x, y)
 
 path = []
 node = goal
 while node in parent:
 path.append(node)
 node = parent[node]
 path.append(start)
 return path[::-1] if goal in visited else [], order
def print_grid(grid, source, goal, path):
 for i in range(len(grid)):
 for j in range(len(grid)):
 if (i, j) == source:
 print('S', end=' ')
 elif (i, j) == goal:
 print('G', end=' ')
 elif (i, j) in path:
 print('*', end=' ')
 else:
 print(grid[i][j], end=' ')
 print()
def main():
 N = random.randint(4, 7)
 grid = generate_grid(N)
 source, goal = get_valid_position(grid, N), 
get_valid_position(grid, N)
 while source == goal:
 goal = get_valid_position(grid, N)
 
 path, order = dfs(grid, source, goal, N)
 
 print("Generated Grid:")
 print_grid(grid, source, goal, path)
 print("\nSource:", source)
 print("Goal:", goal)
 print("\nDFS Path:", path if path else "No path found")
 print("Topological Order:", order)
if __name__ == "__main__":
 main()