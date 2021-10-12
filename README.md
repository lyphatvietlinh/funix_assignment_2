# Introduction
This is a simple project for automated grading student's test answers, and output the scores in a text file.

# Instruction
When run, the program will ask for a filename input, to start grading. The input file should be stored in the same directory with the source code file.

The input file for grading should be in text file format (.txt), with each line represents one student's answers.
```
N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D
N00000021,B,A,C,D,C,C,D,D,C,C,D,B,,B,A,C,B,,A,D,A,A,B,D,
N00000022,B,A,D,A,C,B,D,D,C,C,D,B,A,B,A,,B,A,A,C,A,A,B,A,D
N00000023,,A,D,D,C,B,D,A,C,C,,C,,B,A,C,B,D,A,C,A,A
N00000024,C,C,D,D,C,B,,A,C,C,D,B,A,B,,C,B,D,A,C,A,B,B,,D
```
The graded scores will be saved in an output text file (.txt), with the file name changed to "original_filename_grades.txt", in the same directory. Each line contains one student's code and his score.
```
N00000001,59
N00000002,70
N00000003,84
N00000004,73
N00000005,83
```
# Data Validation
1. The program will first attempt to find and open the file. An error is output if the file cannot be found. 

2. If the file can be found, then it will continue to open the file for data validation: 
   * The first value should be the student code. It should contain the character “N” followed by 8 numeric characters
   * The following number of values should be corresponding to the number of answers, which in this case is 25 answers. 
   * Line with invalid data will be printed out. 
   * A report of total lines including valid and invalid lines will  be printed out

3. Only valid data will be graded and saved into the output file. 

# Grading
Grading will be followed by these policies:
* +4 points for every right answer
* 0 points for every skipped answer
* -1 point for every incorrect answer

Statistics for the file will be printed out (but not saved in the output file):
* Average score
* Highest score
* Lowest score
* Score range
* Median value