import numpy as np


# TASK 1
def checkfile(filename):
    """
    Checks if the file exists before doing further works.

    :param filename: file to check
    :return: boolean on file existence
    """
    print("FILE CHECKING".center(30, "-"))
    try:
        open(filename)
        print("File '{}' founded!".format(filename))
        return True
    except FileNotFoundError:
        print("Could not find file '{}'!".format(filename))
        return False


# TASK 2
def analyze(filename):
    """
    Analyze the file and detect invalid lines before doing other works.

    :param filename: file to check
    :return: Doesn't return anything yet
    """
    print("ANALYSING!".center(30, "-"))
    with open(filename, 'r') as file_object:
        total_lines = 0
        valid_lines = 0
        assignments_dict = dict()
        for line in file_object:
            result = line.strip().split(",")
            if len(result) != 26:
                print("Not enough answers from student: {}".format(result[0]))
            else:
                valid_lines += 1
                assignments_dict[result[0]] = result[1:]
            total_lines += 1
        if valid_lines == total_lines:
            print("No errors found!")
        print("REPORT!".center(30, "-"))
        print("Total lines of data: {}".format(total_lines))
        print("Total valid lines of data: {}".format(valid_lines))
        print("Total invalid lines of data: {}".format(total_lines - valid_lines))
    return assignments_dict


# TASK 3
def grade(assignments_dict):
    print("GRADING!".center(30, "-"))
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".strip().split(",")
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
    score = np.array(list(assignments_dict.values()))
    print("{} students graded!".format(len(assignments_dict)))
    print("Average score: {}".format(score.mean()))
    print("Highest score: {}".format(score.max()))
    print("Lowest score: {}".format(score.min()))
    print("Range of scores: {}".format(score.max() - score.min()))
    print("Median value: {}".format(np.median(score)))
    return assignments_dict


file = input("Input your filename: ")
if checkfile(file):
    assignments = analyze(file)
    scores = grade(assignments)
