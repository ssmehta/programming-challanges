/*
Climbing Stairs

Challenge Description:

You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains a positive integer which is the total number of stairs. e.g.

    10
    20

Output sample:

Print out the number of ways to climb to the top of the staircase. e.g.

    89
    10946
*/

#include <cstdio>
#include <vector>

using namespace std;


int main(int argc, char *argv[]) {
    vector<int> fib;
    fib.push_back(0);
    fib.push_back(1);
    int a = 1, b = 1;
    
    FILE *fp = fopen(argv[1], "r");
    int n;
    
    while(fscanf(fp, "%d\n", &n) != EOF) {
        while(fib.size() <= n) {
            fib.push_back(a + b);
            a = b;
            b = fib.back();
        }
        
        printf("%d\n", fib.at(n));
    }
    
    fclose(fp);
    return 0;
}
