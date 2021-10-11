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
# This is some changes
# This is some changes that was made on the remote repo. Pull before doing local work.
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
        for i, line in enumerate(file_object):
            result = file_object.readline().strip().split(",")
            if len(result) != 26:
                print("Error found at line {}".format(i))
                print(result)
            else:
                valid_lines += 1
            total_lines += 1
        if valid_lines == total_lines:
            print("No errors found!")
        print("REPORT!".center(30, "-"))
        print("Total valid lines of data: {}".format(valid_lines))
        print("Total invalid lines of data: {}".format(total_lines - valid_lines))


file = input("Input your filename: ")
if checkfile(file):
    analyze(file)
