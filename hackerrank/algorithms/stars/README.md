Stars
====

Little John has drawn N stars on his paper. John likes all the stars but not equally. More precisely he likes star number i with weight v<sub>i</sub>. He draws a line that divides the paper into two parts such that each part has a subset of stars in them. Let the weight of each part be the summation of weights of the stars in the part. He wants to draw the line such that the difference in the sum of weights between the two parts is as small as possible while maximizing the smaller part’s weight. Your task is to compute the weight of smaller part corresponding to this desired line. No stars are allowed to be on the line.

### Input:

The first line of the input contains an integer n.

Each of next N lines contains three integers x<sub>i</sub> and y<sub>i</sub> specifying the positions of i<sup>th</sup> star and v<sub>i</sub>.

N is at most 100.

No three points lie on a line.

All the input numbers are between -10<sup>9</sup> and 10<sup>9</sup>.

v<sub>i</sub> is between 1 and 1000.

### Output:

Print an integer being the answer to the test.

### Sample Input:

    10
    748798831 -200797120 595
    -774675771 179630170 159
    -338760201 945958360 750
    955629379 -312997434 516
    755005057 -672683474 405
    -743176829 190325067 86
    -301478753 -718170081 923
    -795908444 985440803 854
    -102868895 671114060 246
    -698209449 12550066 190

### Sample Output:
    
    2358