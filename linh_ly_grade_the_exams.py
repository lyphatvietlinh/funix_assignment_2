import numpy as np
import pandas as pd

# Setting the answer keys
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D" \
	.strip().split(",")
no_of_answers = len(answer_key)


# TASK 1
def check_file(filename: str):
	"""
    Checks if the file exists before doing further works.

    :param filename: file to check
    :return: true/false on file existence
    """
	print("\n" + "FILE CHECKING".center(30, "-") + "\n")
	try:
		open(filename)
		print("File '{}' founded!".format(filename))
		return True
	except FileNotFoundError:
		print("Could not find file '{}'!".format(filename))
		return False


# TASK 2
def check_student_code(code: str):
	"""
    To check if a student number/code is valid

    :param code: student code to check
    :return: true if the code is valid, false if not
    """
	if code[0] != "N":
		return False
	if len(code) != 9:
		return False
	for char in code[1:]:
		if not char.isdigit():
			return False
	return True


def analyze(filename: str):
	"""
    Analyze the file and detect invalid lines before doing other works.

    :param filename: file to check
    :return: dictionary of student_code:graded_score. Return 0 if every
    line is invalid
    """
	print("\n" + "ANALYSING!".center(30, "-") + "\n")
	with open(filename, 'r') as file_object:
		total_lines = 0
		valid_lines = 0
		assignments_dict = dict()

		# Check and validate every line in file for: number of answers,
		# and student code. Store valid data in a dataframe
		for line in file_object:
			result = line.strip().split(",")
			if len(result) - 1 != no_of_answers:
				print("Invalid data - Incorrect number of answers ({})"
					  .format(len(result) - 1))
				print(result)
			elif not check_student_code(result[0]):
				print("Invalid data - Incorrect student code")
				print(result)
			else:
				valid_lines += 1
				assignments_dict[result[0]] = result[1:]
			total_lines += 1

		if valid_lines == total_lines:
			print("No errors found!")

		print("\n" + "REPORTING!".center(30, "-") + "\n")
		print("Total lines of data:".ljust(30, "-") + " {}"
			  .format(total_lines))
		print("Total valid lines of data:".ljust(30, "-") + " {}"
			  .format(valid_lines))
		print("Total invalid lines of data:".ljust(30, "-") + " {}"
			  .format(total_lines - valid_lines))

		if valid_lines == 0:
			return 0
		df = pd.DataFrame(assignments_dict)
		df['Answer'] = answer_key
	return df


# TASK 3
def grade(data: pd.DataFrame):
	"""
    Grade the input assignment dictionary

    :param data: a dataframe with student code as columns
    value = answers
    :return: a dataframe contains key = student code, value = score
    """
	print("\n" + "GRADING!".center(30, "-") + "\n")

	# Grade the score for each student
	result = []
	for column in data.columns[:-1]:
		score = 0
		for i in range(len(data[column])):
			if data[column][i] == data['Answer'][i]:
				score += 4
			elif data[column][i] == "":
				continue
			else:
				score += -1
		result.append(score)

	# Construct new dataframe with student code and score.
	df = pd.DataFrame()
	df['Student'] = data.columns[:-1]
	df['Score'] = result

	# Outputting statistic report
	score = np.array(result)
	print("Number of students graded:".ljust(30, "-")
		  + " {}".format(len(result)))
	print("Average score:".ljust(30, "-")
		  + " {:.2f}".format(score.mean()))
	print("Highest score:".ljust(30, "-")
		  + " {}".format(score.max()))
	print("Lowest score:".ljust(30, "-")
		  + " {}".format(score.min()))
	print("Range of scores:".ljust(30, "-")
		  + " {}".format(score.max() - score.min()))
	print("Median value:".ljust(30, "-")
		  + " {:.2f}".format(np.median(score)))

	# Return the dict with student:score pairs
	return df


# TASK 4
def write_file(data: pd.DataFrame, filename: str):
	"""
    Writes result scores into a file

    :param data: dataframe contains student code and score as key:value
    :param filename: original name of the file that was used for grading
    """
	print("\n" + "EXPORTING RESULTS!".center(30, "-") + "\n")
	filename = filename.replace(".txt", "_grades.txt")
	data.to_csv(filename, index=False, header=False)
	print("Results saved to '{}' successfully!".format(filename))


while True:
	file = input("Input your filename: ")
	if check_file(file):
		file_data = analyze(file)
		file_result = grade(file_data)
		write_file(file_result, file)
	print("\n" + "RESTARTING!".center(30, "-") + "\n")
