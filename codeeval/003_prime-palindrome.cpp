/*
Prime Palindrome

Challenge Description:

Write a program to determine the biggest prime palindrome under 1000.

Input sample:

    None

Output sample:

Your program should print the largest palindrome on stdout. i.e.

    929
*/

#include <cstdio>

using namespace std;


bool isPalindrome(int n) {
    int k = n, m = 0;
    
    do
        m = (10 * m) + (k % 10);
    while((k /= 10) > 0);
    
    return n == m;
}

bool isPrime(int n) {
    if(n < 2)
        return false;
    else if(n == 2 || n == 3)
        return true;
    else if(n % 2 == 0 || n % 3 == 0)
        return false;
    else {
        int i = 6;
        
        while(i * i <= n) {
            if(n % (i - 1) == 0 || n % (i + 1) == 0)
                return false;
            i += 6;
        }
        
        return true;
    }
}


int main(int argc, char *argv[]) {
    int n = 999;
    
    while(n > 1) {
        if(isPalindrome(n) && isPrime(n))
            break;
        n--;
    }
    
    printf("%d\n", n);
    return 0;
}
