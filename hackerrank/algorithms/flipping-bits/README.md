Flipping Bits
=============

You will be given a list of 32-bits unsigned integers. You are required to output the list of the unsigned integers you get by flipping bits in its binary representation (i.e. unset bits must be set, and set bits must be unset).

### Input:

The first line of the input contains the list size *T*. *T* lines follow each line having an integer from the list.

### Output:

Output one line per element from the list with the requested result.

### Sample Input:

    3 
    2147483647
    1 
    0

### Sample Output:

    2147483648 
    4294967294 
    4294967295

### Explanation:

Take 1 for example, as unsigned 32-bits is `00000000000000000000000000000001` and doing the flipping we get `11111111111111111111111111111110` which in turn is `4294967294`.