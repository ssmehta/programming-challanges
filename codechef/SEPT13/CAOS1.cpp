#include <cstdio>

using namespace std;


int main() {
    long T;
    scanf("%ld", &T);
    
    int R, C, X;
    int left, right, top, bottom;
    long total;
    
    char grid[50][50];
    int cpcs[50][50];
    
    
    for(long k = 0; k < T; k++) {
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
        
        for(int i = 0; i < R; i++)
            for(int j = 0; j < C; j++)
                if(cpcs[i][j] > 1)
                    total++;
        
        printf("%ld\n", total);
    }
    
    return 0;
}
