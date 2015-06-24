Random Number Generator
=======================

There is an ideal random number generator, which given a positive integer M can generate any **real number** between 0 to M with equal probability.

Suppose we generate 2 numbers x and y via the generator by giving it 2 positive integers A and B, what’s the probability that x + y is less than C? where C is a positive integer.

### Input:

The first line of the input is an integer N, the number of test cases.

N lines follow. Each line contains 3 positive integers A, B and C.

### Constraints:

All the integers are no larger than 10000.

### Output:

For each output, output a fraction that indicates the probability. The greatest common divisor of each pair of numerator and denominator should be 1.

### Sample Input:

    3
    1 1 1
    1 1 2
    1 1 3

### Sample Output:
    
    1/2
    1/1
    1/1
