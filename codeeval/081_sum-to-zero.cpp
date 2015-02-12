/*
Sum to Zero

Challenge Description:

You are given an array of integers. Count the numbers of ways in which the sum of 4 elements in this array results in zero. 

Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file consist of comma separated positive and negative integers. E.g. 

    2,3,1,0,-4,-1
    0,-1,3,-2

Output sample:

Print out the count of the different number of ways that 4 elements sum to zero. E.g. 

    2
    1
*/

#include <cstdio>
#include <vector>

using namespace std;


char morseChar(char code[]) {
    switch(code[0]) {
        case '.': switch(code[1]) {
            case '/': return 'E';
            
            case '.': switch(code[2]) {
                case '/': return 'I';
                
                case '.': switch(code[3]) {
                    case '/': return 'S';
                    
                    case '.': switch(code[4]) {
                        case '/': return 'H';
                        case '.': return '5';
                        case '-': return '4';
                    }
                    
                    case '-': switch(code[4]) {
                        case '/': return 'V';
                        case '-': return '3';
                    }
                }
                
                case '-': switch(code[3]) {
                    case '/': return 'U';
                    case '.': return 'F';
                    case '-': return '2';
                }
            }
            
            case '-': switch(code[2]) {
                case '/': return 'A';
                
                case '.': switch(code[3]) {
                    case '/': return 'R';
                    case '.': return 'L';
                }
                
                case '-': switch(code[3]) {
                    case '/': return 'W';
                    case '.': return 'P';
                    
                    case '-': switch(code[4]) {
                        case '/': return 'J';
                        case '-': return '1';
                    }
                }
            }
        }
        
        case '-': switch(code[1]) {
            case '/': return 'T';
            
            case '.': switch(code[2]) {
                case '/': return 'N';
                
                case '.': switch(code[3]) {
                    case '/': return 'D';
                    case '-': return 'X';
                    
                    case '.': switch(code[4]) {
                        case '/': return 'B';
                        case '.': return '6';
                    }
                }
                
                case '-': switch(code[3]) {
                    case '/': return 'K';
                    case '.': return 'C';
                    case '-': return 'Y';
                }
            }
            
            case '-': switch(code[2]) {
                case '/': return 'M';
                
                case '.': switch(code[3]) {
                    case '/': return 'G';
                    case '-': return 'Q';
                    
                    case '.': switch(code[4]) {
                        case '/': return 'Z';
                        case '.': return '7';
                    }
                }
                
                case '-': switch(code[3]) {
                    case '/': return 'O';
                    case '.': return '8';
                    
                    case '-': switch(code[4]) {
                        case '.': return '9';
                        case '-': return '0';
                    }
                }
            }
        }
    }
    
    return '\0';
}


int main(int argc, char *argv[]) {
    char code[5];
    int c, n = 0;
    bool is_int = true;
    vector<int> ints;
    
    FILE *fp = fopen(argv[1], "r");
    
    while((c = fgetc(fp)) != EOF) {
        if(c == ' ' && n == 0)
            printf(" ");
        else if(c == ' ' || c == '\n') {
            if(n < 5)
                code[n] = '/';
            
            printf("%c", morseChar(code));
            n = 0;
            
            if(c == '\n')
                printf("\n");
        } else
            code[n++] = c;
    }
    
    fclose(fp);
    return 0;
}
