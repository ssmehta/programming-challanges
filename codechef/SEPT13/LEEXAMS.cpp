#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;


int n, A[50], B[50], P[50];

double computeProbability(int i, double p, vector<int>& used) {
    if(i == n)
        return p / 100;
    
    else {
        double local_p = 0;
        
        if(find(used.begin(), used.end(), A[i]) == used.end()) {
            used.push_back(A[i]);
            local_p += computeProbability(i + 1, P[i], used);
            used.pop_back();
        }
        
        if(find(used.begin(), used.end(), B[i]) == used.end()) {
            used.push_back(B[i]);
            local_p += computeProbability(i + 1, 100 - P[i], used);
            used.pop_back();
        }
        
        return p * local_p / 100;
    }
}

double computeProbability() {
    vector<int> used;
    double p = 0;
    
    used.push_back(A[0]);
    p += computeProbability(1, P[0], used);
    used.pop_back();
    
    used.push_back(B[0]);
    p += computeProbability(1, 100 - P[0], used);
    used.pop_back();
    
    return p;
}



int main() {
    int T;
    scanf("%d", &T);
    
    for(int i = 0; i < T; i++) {
        scanf("%d", &n);
        
        for(int j = 0; j < n; j++)
            scanf("%d %d %d", &P[j], &A[j], &B[j]);
        
        if(n > 16)
            printf("%.9f\n", 0.0);
        else
            printf("%.9f\n", computeProbability());
    }
}
