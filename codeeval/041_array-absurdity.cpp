/*
Array Absurdity

Challenge Description:

Imagine we have an immutable array of size N which we know to be filled with integers ranging from 0 to N-2, inclusive. Suppose we know that the array contains exactly one duplicated entry and that duplicate appears exactly twice. Find the duplicated entry. (For bonus points, ensure your solution has constant space and time proportional to N)

Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Ignore all empty lines. Each line begins with a positive integer(N) i.e. the size of the array, then a semicolon followed by a comma separated list of positive numbers ranging from 0 to N-2, inclusive. i.e eg.

    5;0,1,2,3,0
    20;0,1,10,3,2,4,5,7,6,8,11,9,15,12,13,4,16,18,17,14

Output sample:

Print out the duplicated entry, each one on a new line eg

    0
    4
*/

#include <cstdio>

using namespace std;


int main(int argc, char *argv[]) {
    FILE *fp = fopen(argv[1], "r");
    int N, n, sum;
    
    while(fscanf(fp, "%d;", &N) != EOF) {
        sum = 0;
        
        for(int i = 0; i < N; i++) {
            fscanf(fp, (i < N - 1) ? "%d," : "%d\n", &n);
            sum += n;
        }
        
        printf("%d\n", sum - (N - 1) * (N - 2) / 2);
    }
    
    fclose(fp);
    return 0;
}
