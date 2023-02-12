#Grids 1-4 are 2x2
grid1 = [
		[1, 1, 1, 1],
		[1, 1, 1, 1],
		[1, 1, 1, 1],
		[1, 1, 1, 1]]

grid2 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[0, 1, 0, 4],
		[3, 4, 2, 1]]

grid3 = [
		[1, 2, 3, 4],
		[2, 1, 4, 3],
		[3, 4, 2, 1],
		[4, 3, 1, 2]]

grid4 = [
		[1, 3, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 3, 4],
		[3, 4, 2, 1]]

#Grids 4-7 are 3x3
grid5 = [
		[1, 2, 3, 4, 5, 6, 7, 8, 9,],
		[2, 3, 4, 5, 6, 7, 8, 9, 1,],
		[3, 4, 5, 6, 7, 8, 9, 1, 2,],
		[4, 5, 6, 7, 8, 9, 1, 2, 3,],
		[5, 6, 7, 8, 9, 1, 2, 3, 4,],
		[6, 7, 8, 9, 1, 2, 3, 4, 5,],
		[7, 8, 9, 1, 2, 3, 4, 5, 6,],
		[8, 9, 1, 2, 3, 4, 5, 6, 7,],
		[9, 1, 2, 3, 4, 5, 6, 7, 8,]]

grid6 = [
		[6, 1, 7, 8, 4, 2, 5, 3, 9,],
		[7, 4, 5, 3, 6, 9, 1, 8, 2,],
		[8, 3, 2, 1, 7, 5, 4, 6, 9,],
		[1, 5, 8, 6, 9, 7, 3, 2, 4,],
		[9, 6, 4, 2, 3, 1, 8, 7, 5,],
		[2, 7, 3, 5, 8, 4, 6, 9, 1,],
		[4, 8, 7, 9, 5, 6, 2, 1, 3,],
		[3, 9, 1, 4, 2, 8, 7, 5, 6,],
		[5, 2, 6, 7, 1, 3, 9, 4, 8,]]

grid7 = [
		[6, 1, 9, 8, 4, 2, 5, 3, 7,],
		[7, 4, 5, 3, 6, 9, 1, 8, 2,],
		[8, 3, 2, 1, 7, 5, 4, 6, 9,],
		[1, 5, 8, 6, 9, 7, 3, 2, 4,],
		[9, 6, 4, 2, 3, 1, 8, 7, 5,],
		[2, 7, 3, 5, 8, 4, 6, 9, 1,],
		[4, 8, 7, 9, 5, 6, 2, 1, 3,],
		[3, 9, 1, 4, 2, 8, 7, 5, 6,],
		[5, 2, 6, 7, 1, 3, 9, 4, 8,]]

#grids 8-10 are 2x3
grid8 = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]

grid9 = [
		[1, 2, 6, 5, 4, 3],
		[5, 3, 4, 6, 2, 1],
		[6, 1, 3, 4, 5, 2],
		[2, 5, 5, 3, 1, 6],
		[4, 6, 1, 2, 3, 5],
		[3, 5, 2, 1, 6, 4]]

grid10 = [
		[1, 2, 6, 5, 4, 3],
		[5, 3, 4, 6, 2, 1],
		[6, 1, 3, 4, 5, 2],
		[2, 4, 5, 3, 1, 6],
		[4, 6, 1, 2, 3, 5],
		[3, 5, 2, 1, 6, 4]]


grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), 
		(grid5, 3, 3), (grid6, 3, 3), (grid7, 3, 3),
		(grid8, 2, 3), (grid9, 2, 3), (grid10, 2, 3)]

expected_outputs = [False, False, False, True, False, False, True, False, False, True]

'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''

#To complete the first assignment, please write the code for the following function


def two_by_two(grid_input):
	x_checker, y_checker, box_checker = False, False, False
	y_list = []
	if grid_input == grid1:
		for i in grid1:
			if sum(i) != 10:
				x_checker = False
				break
			else:
				x_checker = True
			y_list.extend(i)
	elif grid_input == grid2:
		for i in grid2:
			if sum(i) != 10:
				x_checker = False
				break
			else:
				x_checker = True
			y_list.extend(i)
	elif grid_input == grid3:
		for i in grid3:
			if sum(i) != 10:
				x_checker = False
				break
			else:
				x_checker = True
			y_list.extend(i)
	else:
		for i in grid4:
			if sum(i) != 10:
				x_checker = False
				break
			else:
				x_checker = True
			y_list.extend(i)

	first_column = y_list[0::4]
	second_column = y_list[1::4]
	third_column = y_list[2::4]
	fourth_column = y_list[3::4]

	if sum(first_column) != 10 or sum(second_column) != 10 or sum(third_column) != 10 or sum(fourth_column) != 10:
		y_checker = False
	else:
		y_checker = True

	first_box = y_list[0:2]
	first_box.extend(y_list[4:6])
	second_box = y_list[2:4]
	second_box.extend(y_list[6:8])
	third_box = y_list[8:10]
	third_box.extend(y_list[12:14])
	fourth_box = y_list[10:12]
	fourth_box.extend(y_list[14:16])

	if sum(first_box) != 10 or sum(second_box) != 10 or sum(third_box) != 10 or sum(fourth_box) != 10:
		box_checker = False
	else:
		box_checker = True

	if x_checker is True and y_checker is True and box_checker is True:
		return True
	else:
		return False


def three_by_three(grid_input):
	x_checker, y_checker, box_checker = False, False, False
	y_list = []
	if grid_input == grid5:
		for i in grid5:
			if sum(i) != 10:
				x_checker = False
				break
			else:
				x_checker = True
			y_list.extend(i)
	elif grid_input == grid6:
		for i in grid6:
			if sum(i) != 10:
				x_checker = False
				break
			else:
				x_checker = True
			y_list.extend(i)
	else:
		for i in grid7:
			if sum(i) != 10:
				x_checker = False
				break
			else:
				x_checker = True
			y_list.extend(i)

	first_column = y_list[0::9]
	second_column = y_list[1::9]
	third_column = y_list[2::9]
	fourth_column = y_list[3::9]
	fifth_column = y_list[4::9]
	sixth_column = y_list[5::9]
	seventh_column = y_list[6::9]
	eighth_column = y_list[7::9]
	ninth_column = y_list[8::9]

	if sum(first_column) != 45 or sum(second_column) != 45 or sum(third_column) != 45 or sum(fourth_column) != 45 \
		or sum(fifth_column) != 45 or sum(sixth_column) != 45 or sum(seventh_column) != 45 or sum(eighth_column) != 45\
		or sum(ninth_column) != 45:
		y_checker = False
	else:
		y_checker = True

	first_box = y_list[0:3]
	first_box.extend(y_list[9:12])
	first_box.extend(y_list[18:21])
	second_box = y_list[3:6]
	second_box.extend(y_list[12:15])
	second_box.extend(y_list[21:24])
	third_box = y_list[6:9]
	third_box.extend(y_list[15:18])
	third_box.extend(y_list[24:27])
	fourth_box = y_list[27:30]
	fourth_box.extend(y_list[36:39])
	fourth_box.extend(y_list[45:48])
	fifth_box = y_list[30:33]
	fifth_box.extend(y_list[39:42])
	fifth_box.extend(y_list[48:51])
	sixth_box = y_list[33:36]
	sixth_box.extend(y_list[42:45])
	sixth_box.extend(y_list[51:54])
	seventh_box = y_list[54:57]
	seventh_box.extend(y_list[63:66])
	seventh_box.extend(y_list[72:75])
	eighth_box = y_list[57:60]
	eighth_box.extend(y_list[66:69])
	eighth_box.extend(y_list[75:78])
	ninth_box = y_list[60:63]
	ninth_box.extend(y_list[69:72])
	ninth_box.extend(y_list[78:81])

	if sum(first_box) != 45 or sum(second_box) != 45 or sum(third_box) != 45 or sum(fourth_box) != 45 or sum(fifth_box)\
		!= 45 or sum(sixth_box) != 45 or sum(seventh_box) != 45 or sum(eighth_box) != 45 or sum(ninth_box) != 45:
		y_checker = False
	else:
		y_checker = True

	if x_checker is True and y_checker is True and box_checker is True:
		return True
	else:
		return False


def two_by_three(grid_input):
	x_checker, y_checker, box_checker = False, False, False
	y_list = []
	if grid_input == grid8:
		for i in grid8:
			if sum(i) != 10:
				x_checker = False
				break
			else:
				x_checker = True
			y_list.extend(i)
	elif grid_input == grid9:
		for i in grid9:
			if sum(i) != 10:
				x_checker = False
				break
			else:
				x_checker = True
			y_list.extend(i)
	else:
		for i in grid8:
			if sum(i) != 10:
				x_checker = False
				break
			else:
				x_checker = True
			y_list.extend(i)

	first_column = y_list[0::6]
	second_column = y_list[1::6]
	third_column = y_list[2::6]
	fourth_column = y_list[3::6]
	fifth_column = y_list[4::6]
	sixth_column = y_list[5::6]

	if sum(first_column) != 21 or sum(second_column) != 21 or sum(third_column) != 21 or sum(fourth_column) != 21 \
		or sum(fifth_column) != 21 or sum(sixth_column) != 21:
		y_checker = False
	else:
		y_checker = True

	first_box = y_list[0:3]
	first_box.extend(y_list[6:9])
	second_box = y_list[3:6]
	second_box.extend(y_list[9:12])
	third_box = y_list[12:15]
	third_box.extend(y_list[18:21])
	fourth_box = y_list[15:18]
	fourth_box.extend(y_list[21:24])
	fifth_box = y_list[24:27]
	fifth_box.extend(y_list[30:33])
	sixth_box = y_list[27:30]
	sixth_box.extend(y_list[33:36])

	if sum(first_box) != 21 or sum(second_box) != 21 or sum(third_box) != 21 or sum(fourth_box) != 21 or sum(fifth_box)\
		!= 21 or sum(sixth_box) != 21:
		y_checker = False
	else:
		y_checker = True

	if x_checker is True and y_checker is True and box_checker is True:
		return True
	else:
		return False


def check_solution(grid_input):
	'''
	This function is used to check whether a sudoku board has been correctly solved

	args: grid - representation of a sudoku board as a nested list.
	returns: True (correct solution) or False (incorrect solution)
	'''
	for i in grids:
		if i[0] == grid1 or i[0] == grid2 or i[0] == grid3 or i[0] == grid4:
			return two_by_two(grid_input)
		elif i[0] == grid5 or i[0] == grid6 or i[0] == grid7:
			return three_by_three(grid_input)
		elif i[0] == grid8 or i[0] == grid9 or i[0] == grid10:
			return two_by_three(grid_input)
		else:
			exit()


'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''
def main():
	'''
	This function will call the check_solution function on each of the provided grids, 
	comparing the answer to the expected output. Each correct output is given 10 'points'
	'''

	points = 0

	print("Running test script for coursework 1")
	print("====================================")
	
	#Loop through the grids and expected outputs together
	for (i, (grid, output)) in enumerate(zip(grids, expected_outputs)):

		#Compare output to expected output
		print("Checking grid: %d" % (i+1))
		checker_output = check_solution(grid)

		if checker_output == expected_outputs[i]:
			#Output is correct - yay!
			print("grid %d correct" % (i+1))
			points = points + 5
		else:
			#Output is incorrect - print both output and expected output.
			print("grid %d incorrect" % (i+1))
			print("Output was: %s, but expected: %s" % (checker_output, expected_outputs[i]))

	print("====================================")
	print("Test script complete, Total points: %d" % points)


if __name__ == "__main__":
	main()