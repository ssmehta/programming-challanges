#include <cstdio>

using namespace std;


int main() {
    int T;
    scanf("%d", &T);
    
    int R, C, X;
    int left, right, top, bottom;
    long total;
    
    char grid[500][500];
    int cpcs[500][500];
    
    int primes[] = {
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,
        149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
        227, 229, 233, 239, 241, 251
    };
    
    
    for(int k = 0; k < T; k++) {
        scanf("%d %d", &R, &C);
        
        for(int i = 0; i < R; i++) {
            scanf("%s", grid[i]);
            
            for(int j = 0; j < C; j++)
                cpcs[i][j] = R;
        }
        
        
        for(int i = 0; i < R; i++) {
            left = 0; right = 0;
            
            for(int j = 0; j < C; j++) {
                if(grid[i][j] == '#') {
                    left = 0;
                    cpcs[i][j] = 0;
                } else {
                    cpcs[i][j] = (left < cpcs[i][j]) ? left : cpcs[i][j];
                    left++;
                }
                
                if(grid[i][C - j - 1] == '#') {
                    right = 0;
                    cpcs[i][C - j - 1] = 0;
                } else {
                    cpcs[i][C - j - 1] = (right < cpcs[i][C - j - 1]) ? right : cpcs[i][C - j - 1];
                    right++;
                }
            }
        }
        
        for(int j = 0; j < C; j++) {
            top = 0; bottom = 0;
            
            for(int i = 0; i < R; i++) {
                if(grid[i][j] == '#') {
                    top = 0;
                    cpcs[i][j] = 0;
                } else {
                    cpcs[i][j] = (top < cpcs[i][j]) ? top : cpcs[i][j];
                    top++;
                }
                
                if(grid[R - i - 1][j] == '#') {
                    bottom = 0;
                    cpcs[R - i - 1][j] = 0;
                } else {
                    cpcs[R - i - 1][j] = (bottom < cpcs[R - i - 1][j]) ? bottom : cpcs[R - i - 1][j];
                    bottom++;
                }
            }
        }
        
        
        total = 0;
        
        for(int i = 0; i < R; i++) {
            for(int j = 0; j < C; j++) {
                int n = 0;
                
                while(n < 54 && primes[n++] <= cpcs[i][j])
                    total++;
            }
        }
        
        printf("%ld\n", total);
    }
    
    return 0;
}
