#include <cstdio>

using namespace std;


long long gcd(long long n, long long m) {
    long long temp;
    
    while(m > 0) {
        temp = m;
        m = n % m;
        n = temp;
    }
    
    return n;
}


int main() {
    int T;
    scanf("%d", &T);
    
    long long N;
    long long n, d, k;
    bool skip;
    
    for(long long i = 0; i < T; i++) {
        scanf("%Ld", &N);
        n = 0; d = N * N; skip = false;
        
        for(long long j = 1; j * j < N + 1; j++) {
            if(skip || j * (j + 1) > N)
                skip = true;
            
            if((j + 1) * (j + 1) < N + 1 || !skip)
                n += j * ((N / j) - (N / (j + 1)));
            n += N / j;
        }
        
        k = gcd(n, d);
        printf("%Ld/%Ld\n", n / k, d / k);
    }
    
    return 0;
}
