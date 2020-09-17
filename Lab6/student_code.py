import common

def drone_flight_planner (map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount):


	#initialize vlaues of delivery fee and drone repair cost
	for x in range(6):
		for y in range(6):
			if map[y][x] == 2:
				values[y][x] = delivery_fee
			if map[y][x] == 3:
				values[y][x] = -dronerepair_cost

	convergence = 100

	while convergence > 0.0001:
		convergence = 0
		for x in range(6):
			for y in range(6):
				if map[y][x] == 2 or map[y][x]==3:
					continue

				max_value = float('-inf')
				max_policy = 0

				new_valuey_plus = y+1
				new_valuey_minus = y-1
				new_valuex_plus = x+1
				new_valuex_minus= x-1
				if y+1 > 5:
					new_valuey_plus = y
				if y-1 < 0:
					new_valuey_minus = y
				if x+1 > 5:
					new_valuex_plus = x
				if x-1 < 0:
					new_valuex_minus = x

				value_sf = 0.7*(-battery_drop_cost + discount * (values[new_valuey_plus][x])) + .15*(-battery_drop_cost + discount*(values[y][new_valuex_plus])) + .15*(-battery_drop_cost + discount*(values[y][new_valuex_minus]))
				SOUTH_OFF = (value_sf, common.constants.SOFF)
				if max_value < SOUTH_OFF[0]:
					max_value = SOUTH_OFF[0]
					max_policy = SOUTH_OFF[1]


				value_wf = 0.7*(-battery_drop_cost + discount * (values[y][new_valuex_minus])) + .15*(-battery_drop_cost + discount*(values[new_valuey_minus][x])) + .15*(-battery_drop_cost + discount*(values[new_valuey_plus][x]))
				WEST_OFF = (value_wf, common.constants.WOFF)
				if max_value < WEST_OFF[0]:
					max_value = WEST_OFF[0]
					max_policy = WEST_OFF[1]

				value_nf = 0.7*(-battery_drop_cost + discount * (values[new_valuey_minus][x])) + .15*(-battery_drop_cost + discount*(values[y][new_valuex_plus])) + .15*(-battery_drop_cost + discount*(values[y][new_valuex_minus]))
				NORTH_OFF = (value_nf, common.constants.NOFF)
				if max_value < NORTH_OFF[0]:
					max_value = NORTH_OFF[0]
					max_policy = NORTH_OFF[1]

				value_ef = 0.7*(-battery_drop_cost + discount * (values[y][new_valuex_plus])) + .15*(-battery_drop_cost + discount*(values[new_valuey_minus][x])) + .15*(-battery_drop_cost + discount*(values[new_valuey_plus][x]))
				EAST_OFF = (value_ef, common.constants.EOFF)
				if max_value < EAST_OFF[0]:
					max_value =  EAST_OFF[0]
					max_policy = EAST_OFF[1]


				value_so = 0.8*(2*-battery_drop_cost + discount * (values[new_valuey_plus][x])) + .10*(2*-battery_drop_cost + discount*(values[y][new_valuex_plus])) + .10*(2*-battery_drop_cost + discount*(values[y][new_valuex_minus]))
				SOUTH_ON = (value_so, common.constants.SON)
				if max_value < SOUTH_ON[0]:
					max_value =  SOUTH_ON[0]
					max_policy = SOUTH_ON[1]

				value_wo = 0.8*(2*-battery_drop_cost + discount * (values[y][new_valuex_minus])) + .10*(2*-battery_drop_cost + discount*(values[new_valuey_minus][x])) + .10*(2*-battery_drop_cost + discount*(values[new_valuey_plus][x]))
				WEST_ON = (value_wo, common.constants.WON)
				if max_value < WEST_ON[0]:
					max_value = WEST_ON[0]
					max_policy = WEST_ON[1]

				value_no = 0.8*(2*-battery_drop_cost + discount * (values[new_valuey_minus][x])) + .10*(2*-battery_drop_cost + discount*(values[y][new_valuex_plus])) + .10*(2*-battery_drop_cost + discount*(values[y][new_valuex_minus]))
				NORTH_ON= (value_no, common.constants.NON)
				if max_value < NORTH_ON[0]:
					max_value = NORTH_ON[0]
					max_policy = NORTH_ON[1]

				value_eo = 0.8*(2*-battery_drop_cost + discount * (values[y][new_valuex_plus])) + .10*(2*-battery_drop_cost + discount*(values[new_valuey_minus][x])) + .10*(2*-battery_drop_cost + discount*(values[new_valuey_plus][x]))
				EAST_ON= (value_eo, common.constants.EON)
				if max_value < EAST_ON[0]:
					max_value =  EAST_ON[0]
					max_policy = EAST_ON[1]



				convergence += abs(values[y][x] - max_value)
				values[y][x] = max_value
				policies[y][x] = max_policy


	#find starting position and return its value
	for x in range(6):
		for y in range(6):
			if map[y][x] == 1:
				return values[y][x]
