/*
Following Integer

Challenge Description:

Credits: This challenge has appeared in a past google competition

You are writing out a list of numbers.Your list contains all numbers with exactly Di digits in its decimal representation which are equal to i, for each i between 1 and 9, inclusive. You are writing them out in ascending order. For example, you might be writing every number with two '1's and one '5'. Your list would begin 115, 151, 511, 1015, 1051. Given N, the last number you wrote, compute what the next number in the list will be. The number of 1s, 2s, ..., 9s is fixed but the number of 0s is arbitrary.

Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will contain an integer n < 10^6

Output sample:

For each line of input, generate a line of output which is the next integer in the list.
*/

#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;


int main(int argc, char *argv[]) {
    FILE *fp = fopen(argv[1], "r");
    vector<int> chars;
    int n, zeros;
    
    while(fscanf(fp, "%d\n", &n) != EOF) {
        zeros = 0;
        chars.clear();
        
        while(n > 0) {
            chars.insert(chars.begin(), n % 10);
            
            if(n % 10 == 0)
                zeros++;
            n /= 10;
        }
        
        if(!next_permutation(chars.begin(), chars.end())) {
            chars.insert(chars.begin(), chars[zeros]);
            chars[zeros + 1] = 0;
        }
        
        for(vector<int>::iterator it = chars.begin(); it != chars.end(); ++it)
            printf("%d", *it);
        printf("\n");
    }
    
    fclose(fp);
    return 0;
}
