import common

def df_search(map):
	found = False
	visited = [[0 for i in range(common.constants.MAP_WIDTH)] for j in range(common.constants.MAP_HEIGHT)]
	parent =[[0 for i in range(common.constants.MAP_WIDTH)] for j in range(common.constants.MAP_HEIGHT)]
	frontier = []

	#find starting point
	for y in range(0,common.constants.MAP_HEIGHT):
		for x in range(0,common.constants.MAP_WIDTH):
			if map[y][x] == 2:
				start = (y,x)

	frontier.append(start)
	# mark as visited
	visited[start[0]][start[1]] = 1

	while frontier:
		current = frontier.pop()
		visited[current[0]][current[1]] = 1

		if map[current[0]][current[1]] != 3:


			if (current[0] - 1) >= 0 and map[current[0] - 1][current[1]] != 1 and visited[current[0] - 1][current[1]] == 0:
				frontier.append((current[0] - 1, current[1]))
				parent[current[0] - 1][current[1]] = (current[0], current[1])

			if (current[1] - 1) >= 0 and map [current[0]][current[1] - 1] != 1 and visited[current[0]][current[1] - 1] == 0:
				frontier.append((current[0],current[1]-1))
				parent[current[0]][current[1] - 1] = (current[0],current[1])

			if current[0] + 1 < common.constants.MAP_HEIGHT and map[current[0] + 1][current[1]] != 1 and visited[current[0] + 1][current[1]] == 0:
				frontier.append((current[0] + 1,current[1]))
				parent[current[0] + 1][current[1]] = (current[0],current[1])

			if (current[1] +  1) < common.constants.MAP_WIDTH and map[current[0]][current[1]+  1] != 1 and visited[current[0]][current[1] +  1] == 0:
				frontier.append((current[0],current[1] + 1))
				parent[current[0]][current[1] + 1] = (current[0],current[1])

		elif map[current[0]][current[1]] == 3:
			goal = current
			found = True
			break

		else:
			found = False
			return found

	#mark visted with a 4
	for y in range(0, common.constants.MAP_HEIGHT):
		for x in range(0, common.constants.MAP_WIDTH):
			if visited[y][x] == 1:
				map[y][x] = 4

	#mark path with 5's using parents
	while current != start and found == True:
		map[current[0]][current[1]] = 5
		current = parent[current[0]][current[1]]

	if current == start and found == True:
		map[current[0]][current[1]] = 5

	return found





def bf_search(map):
	found = False
	visited = [[0 for i in range(common.constants.MAP_WIDTH)] for j in range(common.constants.MAP_HEIGHT)]
	parent =[[0 for i in range(common.constants.MAP_WIDTH)] for j in range(common.constants.MAP_HEIGHT)]
	frontier = []

	#find starting point
	for y in range(0,common.constants.MAP_HEIGHT):
		for x in range(0,common.constants.MAP_WIDTH):
			if map[y][x] == 2:
				start = (y,x)

	frontier.append(start)
	# mark as visited
	visited[start[0]][start[1]] = 1

	while frontier:
		current = frontier.pop(0)
		visited[current[0]][current[1]] = 1

		if map[current[0]][current[1]] != 3:

			if (current[1] +  1) < common.constants.MAP_WIDTH and map[current[0]][current[1]+  1] != 1 and visited[current[0]][current[1] +  1] == 0:
				frontier.append((current[0],current[1] + 1))
				parent[current[0]][current[1] + 1] = (current[0],current[1])

			if current[0] + 1 < common.constants.MAP_HEIGHT and map[current[0] + 1][current[1]] != 1 and visited[current[0] + 1][current[1]] == 0:
				frontier.append((current[0] + 1,current[1]))
				parent[current[0] + 1][current[1]] = (current[0],current[1])

			if (current[1] - 1) >= 0 and map [current[0]][current[1] - 1] != 1 and visited[current[0]][current[1] - 1] == 0:
				frontier.append((current[0],current[1]-1))
				parent[current[0]][current[1] - 1] = (current[0],current[1])

			if (current[0] - 1) >= 0 and map[current[0] - 1][current[1]] != 1 and visited[current[0] - 1][current[1]] == 0:
				frontier.append((current[0] - 1, current[1]))
				parent[current[0] - 1][current[1]] = (current[0], current[1])
			

		elif map[current[0]][current[1]] == 3:
			goal = current
			found = True
			break

		else:
			found = False
			return found

	#mark visted with a 4
	for y in range(0, common.constants.MAP_HEIGHT):
		for x in range(0, common.constants.MAP_WIDTH):
			if visited[y][x] == 1:
				map[y][x] = 4

	#mark path with 5's using parents
	while current != start and found == True:
		map[current[0]][current[1]] = 5
		current = parent[current[0]][current[1]]

	if current == start and found == True:
		map[current[0]][current[1]] = 5

	return found
