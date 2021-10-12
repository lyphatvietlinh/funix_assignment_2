# --------------------------------------------------------------------
# FUNIX ASSIGNMENT 2
# --------------------------------------------------------------------
import numpy as np

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
		# and student code. Store valid data in a dict with key:value pair
		# as student:answers
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

	return assignments_dict


# TASK 3
def grade(assignments_dict: dict):
	"""
    Grade the input assignment dictionary

    :param assignments_dict: dict type input, with key = student code,
    value = answers
    :return: a dict contains key = student code, value = score
    """
	print("\n" + "GRADING!".center(30, "-") + "\n")

	# Loop through every student:answers pair in the dict, compare with
	# answer_key for grading, then replace the answers in the dict with
	# the graded score
	for student, result in assignments_dict.items():
		score = 0
		for i in range(len(result)):
			if result[i] == answer_key[i]:
				score += 4
			elif result[i] == "":
				pass
			else:
				score += -1
		assignments_dict[student] = score

	# Outputting statistic report
	score = np.array(list(assignments_dict.values()))
	print("Number of students graded:".ljust(30, "-")
		  + " {}".format(len(assignments_dict)))
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
	return assignments_dict


# TASK 4
def write_file(scores_dict: dict, filename: str):
	"""
    Writes result scores into a file

    :param scores_dict: dict contains student code and score as key:value
    :param filename: original name of the file that was used for grading
    """
	print("\n" + "EXPORTING RESULTS!".center(30, "-") + "\n")
	filename = filename.replace(".txt", "_grades.txt")
	with open(filename, "w+") as file_object:
		for key, value in scores_dict.items():
			file_object.write(key + "," + str(value) + "\n")
	print("Results saved to '{}' successfully!".format(filename))


while True:
	file = input("Input your filename: ")
	if check_file(file):
		assignments = analyze(file)
		if assignments:
			scores = grade(assignments)
			write_file(scores, file)
		else:
			print("No valid line to grade!")
	print("\n" + "RESTARTING!".center(30, "-") + "\n")
