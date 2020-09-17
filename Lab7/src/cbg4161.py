import common


def part_one_classifier(data_train, data_test):

	weight =[0.0,0.0,0.0]
	incorrect = 1
	while incorrect > 0:
		incorrect = 0
		for y in range(common.constants.TRAINING_SIZE):
			f = [data_train[y][0], data_train[y][1], 1.0]
			prediction = multiply(weight, f)
			if prediction >= 0:
				label = 1
			else:
				label = 0
			if label != data_train[y][2]:
				incorrect+= 1
				for x in range(3):
					weight[x]+= (data_train[y][2]-label) * f[x]


	#label test data
	for y in range(common.constants.TEST_SIZE):
		f = [data_test[y][0], data_test[y][1], 1]
		prediction_test = multiply(weight, f)
		if prediction_test >= 0:
			label2 = 1
		else:
			label2 = 0
		data_test[y][2] = label2

	return


def part_two_classifier(data_train, data_test):
	weights =[[0 for i in range(3)] for j in range(9)]
	incorrect = float('inf')

	while 0.07 <= float(incorrect/float(common.constants.TRAINING_SIZE)):

		incorrect = 0
		for y in range(common.constants.TRAINING_SIZE):
			f = [data_train[y][0], data_train[y][1], 1]
			prediction = argmax_multiply(weights, f)
			if prediction != data_train[y][2]:
				incorrect+=1
				for x in range(3):
					weights[int(data_train[y][2])][x] += f[x] * 0.01
				for x in range(3):
					weights[prediction][x]-= f[x] * 0.01


	#label test data
	for y in range(common.constants.TEST_SIZE):
		f = [data_test[y][0], data_test[y][1], 1]
		prediction_test = argmax_multiply(weights, f)
		data_test[y][2] = prediction_test

	return




#HELPER FUNCTIONS

def multiply(vector1, vector2):
	product = 0
	for x in range(3):
		product += vector1[x] * vector2[x]

	return product

def argmax_multiply(weights, f):
	args = [0,0,0,0,0,0,0,0]
	max_index = 0
	max_prod = float('-inf')
	for y in range(9):
		product = 0
		for x in range(3):
			product += weights[y][x] * f[x]
		if product > max_prod:
			max_prod = product
			max_index = y

	return max_index #CHECK
