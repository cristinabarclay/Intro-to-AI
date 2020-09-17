import common

def astar_search(map):

	visited = [[0 for i in range(common.constants.MAP_WIDTH)] for j in range(common.constants.MAP_HEIGHT)]
	parent =[[0 for i in range(common.constants.MAP_WIDTH)] for j in range(common.constants.MAP_HEIGHT)]
	frontier =[]

	found = False

	#find starting point
	for y in range(0,common.constants.MAP_HEIGHT):
		for x in range(0,common.constants.MAP_WIDTH):
			if map[y][x] == 2:
				start = (y,x)

	#find goal
	for y in range(0,common.constants.MAP_HEIGHT):
		for x in range(0,common.constants.MAP_WIDTH):
			if map[y][x] == 3:
				end = (y,x)


	frontier.append(start)


	while frontier:

		#choose what to expand by heuristic
		current = frontier.pop(heuristic(frontier, end, map, parent))
		#mark as visited
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

def heuristic(frontier, end, map, parent):

	shortest_distance = 1000
	shortest_node = (10,10)
	shortest_index = 1000



	#Manhattan Distance between two points (x1, y1) and (x2, y2) is:
	for index, node in enumerate(frontier):
		x = node[0] - end[0]
		abs_x = abs(x)
		y = node[1] - end[1]
		abs_y = abs(y)
		d = abs_x + abs_y
	

		cost_of_n = cost(node, map, parent)

		distance = d + cost_of_n


		if distance < shortest_distance:
			shortest_distance = distance
			shortest_node = node
			shortest_index = index

		#if same, determine by x value
		if distance == shortest_distance:
			if node[1] < shortest_node[1]:
				shortest_node = node
				shortest_index = index

				#if same x, determine by y
			elif shortest_node[1] == node[1]:
				if node[0] < shortest_node[0]:
					shortest_node = node
					shortest_index = index

	return shortest_index

def cost(node, map, parent):
	cost_count = 0
	while map[node[0]][node[1]] != 2:
		cost_count = cost_count + 1
		node = parent[node[0]][node[1]]

	return cost_count
