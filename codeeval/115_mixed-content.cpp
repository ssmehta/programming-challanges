/*
Mixed Content

Challenge Description:

You have a string of words and digits divided by comma. Write a program which separates words with digits. You shouldn't change the order elements.

Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

    8,33,21,0,16,50,37,0,melon,7,apricot,peach,pineapple,17,21
    24,13,14,43,41

Output sample:

    melon,apricot,peach,pineapple|8,33,21,0,16,50,37,0,7,17,21
    24,13,14,43,41
*/

#include <cstdio>
#include <vector>

using namespace std;


int main(int argc, char *argv[]) {
    char word[1024];
    int c, n = 0, words = 0;
    bool is_int = true;
    vector<int> ints;
    
    FILE *fp = fopen(argv[1], "r");
    
    while((c = fgetc(fp)) != EOF) {
        if(c == ',' || c == '\n') {
            if(is_int) {
                int order = 1, k = 0;
                
                for(int i = 1; i <= n; i++, order *= 10)
                    k += (word[n - i] - 48) * order;
                
                ints.push_back(k);
            } else {
                if(words > 0)
                    printf(",");
                
                for(int i = 0; i < n; i++)
                    printf("%c", word[i]);
                
                words++;
            }
            
            if(c == '\n') {
                if(!ints.empty()) {
                    if(words > 0)
                        printf("|");
                    
                    for(vector<int>::iterator it = ints.begin(); it != ints.end(); ++it) {
                        if(it != ints.begin())
                            printf(",");
                        printf("%d", *it);
                    }
                }
                
                printf("\n");
                ints.clear();
                words = 0;
            }
            
            n = 0;
            is_int = true;
        } else {
            word[n++] = c;
            is_int *= (c >= '0' && c <= '9');
        }
    }
    
    fclose(fp);
    return 0;
}
