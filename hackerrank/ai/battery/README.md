Laptop Battery Life
===================

Fred is a very predictable man. For instance, when he uses his laptop, all he does is watch TV shows. He always watches until his battery dies. He is also a very meticulous man. He has kept logs of every time he has charged his laptop, which includes how long he charged his laptop for and how long he was able to watch TV for afterwards. Now, Fred wants to use this log to predict how long he will be able to watch TV for when he starts so that he can plan his activites after watching his TV shows accordingly.

### Challenge:

You will be able to access Fred’s laptop charging log by reading from the file “trainingdata.txt”. The training data file will consist of 100 lines, each with 2 comma-separated numbers. The first number denotes the amount of time the laptop was charged and the second denotes the amount of time the battery lasted. The training data file can be downloaded [here](https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt) (this will be the same training data used when your program is run). The input for each of the test cases will consist of exactly 1 number rounded to 2 decimal places. For each input, output 1 number: the amout of time you predict his battery will last.

### Sample Input:

    1.50

### Sample Output:

    3.00

### Scoring:

Your score will be 10-X, where X is the sum of the distances you are from expected answer of each test case. For instance if there are 2 test cases with expected answer 4 and you print 3 for the first one and 6 for the second one your score will be 10-(1+2) = 7.
